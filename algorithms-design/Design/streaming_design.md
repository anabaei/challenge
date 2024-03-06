

# Design Steam Processing

#### All designs are in 3 main Categories 
* `Online Processing`: is user transactions and user responses, response fast, uber
* `Batch Processing`: email subscription, push notifications. 
TB or GB of data in batch so we need something to distribute them and output is also huge so apache spark is a choice. 
 *     
* `Steam Processing`: data always arriving, act if data arrives.
Stream processing is application generated data and instantly coming in. 
* Difference between Online systems which has ACID philosophy to make sure data has devlivered and we can't lost some orders, but system processing is fire and forget, it means it is okay if you drop some data

* `Map Reducer` is used both in batch and stream processing. Map reducers are like `Apache Spark`. Spark has spark streaming feature

### Stream Processing 
* Always moving data, analyze incoming data, growth in data size and velocity, any application monitoring tools are example of stream processing. 
* `Fraud detection` is another example which we need to response immediately
* `Predictive maintence and trend detection`: bubble up what is trending
* `Cameras IoT`: detection of human/animals needs to send 
* `Activity Tracking`: 


#### Design in High Level

* `data payload usually is small` because you have 1000/sec going through so it is better to keep payload small
* `publisher and producer` generate data
* `consumer and subscriber` consume data
* between generator and consumer there is a `queue` like kafka, rabbitmq, etc.. 
* `no downtime` means the flow of code is a forever loop. There is no termination of the code, we try to best not have downtime but if it happens it should back to state where it was and continue


#### Application Monitoring Tool (Designing Problem)

* Imagine you have 10000 servers each one emit 2000/s such as cpu utilization to send central brain and dashboard to display
 given serverId in time window of 2 days with granuarily of 1 min

### Queues inMemory & Disk
* RabbitMQ is in memory style queue and Kafka is in Disk style 

## Distributed Queues
#### RabbitMQ
* `RabbitMQ` and `AmazonMQ` are over on MQ, it is older than kafka and originated when computers were not easily available as now.  

* It supports low latency, priority because it is in memory but then Limited with large data 

* `Producer` generates data. Producers can be application, logstash, flowing or anything
* `Messages` are data in transit or payloads 
* `routing keys`
* `consumer` entities that act on data like application or spark streaming apps
* `Exchanges` has three parts in rabbit mq. 
    * `Direct`: one to one queue 
    * `Topic`: one to many queue
    * `Fanout`: one to all queue

* Consumer binds to `queues`, it attach itself to queues and data passes to consumer when exchange allow
* `rabbitmq` is smart enough when push to any queue, then it remove data
* message order delivery guaranteed
* You can add ranking to payload then broker can figure out to tell what is priority of the message
* smart broker and dumb client where clients only display data
* rabbitmq is push model not other way

#### Kafka
* Kafka is pull, client pull data from kafka
* More latency because it is in disk
* Kafka perform at very high throughput level of incoming data, and the order is not that important

* `Producers`: means some agents constantly generating data code, utility, fluentbit, utilliyy 
* everything written in file which called them segments, it never delete unless u delete
* `Topic` : Set of similar messages, any event can be a topic
* `partition` each topic has one or more  partitions for scalability solutions, it has entity which allows to write
* `consumer` read queues one by one which is called offseting
* kafka is good for saving huge amount of data on daily like how many clicks on something happened but it is not good for making queries 

![kafka](https://github.com/anabaei/Javascript/assets/7471619/6407eb85-2cde-4ab7-91f8-3cc799547d11)

# General approach
* Ask questions and write functional requirements, in a way you are defining end points 
* write down non functional requirements, 
* Always try to draw a simple working first diagrams using microservices to let it work
* half the rest scale, perfomance, availability 
### Functional Requirements questions
* How many users use the dashboard? number of users in total
* How often metrics emitted? (in case desiging)
* What is granularity? it means when we query thise data are in what time like in 1 min
* what is acceptable latency, 1-2 seconds usually is okay for hot data
* Is there a need to build alerting system, (if time exist)

* Then go with a simple sketch 
* Agent sent data, or generate data to stateless REST API server,
* Then server queues data into queues like kafka
* kafka send data to aggregate into server and save into database and cache (at cache we save garnularity which easily can retrieve from FE)
* There is a need to look up by keys, Users need a specific cpu, ip data, the best way is using relational db which makes this queries faster
* 
* users can retrieve data from REST, rest either get data from cache or database

![src](https://github.com/anabaei/Javascript/assets/7471619/9d558f4b-c211-44bd-b200-9bed1bb8d344)


#### Deep Dive

#### Data Payload
* A json object
```
serverId: can have 10k different uuid or hashids 
metricId: can have 2k different possible values like cpu, ram,  
value: (value of metric)
ts: of origination of metric
```
* integers : 8-bit 1 byte, 16-bit: 2 byte,
* MD5 (128-bit hash): Requires 16 bytes.
* payload Size: 4byte each -> 16byte 
* 32-bit fixed-size binary timestamp: 4 bytes, if stored as 64 bit then 8 bytes
* At Acsii and UTF-8 encoding each charactor takes 1 byte. At UTF-16 and 32 it takes 2 and 4 bytes.
* 10k (number of servers) * 2k(metrics) * 16 = size of queue input 320 m/s

##### Agent
* What is agent?
* Potentially design of it?
* How often to send data?
* Failur scenarios?
* Agents running on routes and switches and send data to server. 
* agnostic to product
* Generator data can send data each one seconds which cause overwhelming of network, can batch data and send each 15 seconds
* Retries: If agent send data but data get lost, so it can try expoentially back off= once you try if it fails it waits `jitter` provides you solution for that,  
* IF there are many agents and all retry to send data at the same time then you start competing, for resources. So we should seperate retries time interval for avoiding this
* 

##### REST API
* Imagine we have load balancer in front of REST API and it distribute data to the services, and send data to the queue..
* It sends 320mb/s to queues

##### Queue
* Here we use Kafka Styling queue. In this case we have answer what are topics, how many partitions, and replications
* `Topics`: Each matrics we can create one topic and each topic can have different partitions. Since we assume there are 2k matrics so this queue can have 2k topics, one topic per metric
* If we put all data since they have all same payload to one topic, there could be problem in reading queues since there would be mixed data from different topics, then workers who reads queues have simpler job. Also it is less scaleable if we put all into one topic. There are some hot topics which they need to be scale seperatelly 
* How many partitions? partiotions means distribute your data write volume across n number of spinning disks(n means partitions). We have 320 mbyte/s as throughput to the queue so need partitions to handle it. It is give best in class MB per second is 100. Kafka is disk based. Since we need at more than 3 partitions to allow to write on the disk( 320/100 = 3 + .2) ~ 4 partitions. More partition is more cost

##### Worker
* Worker reads from queues.
* Workers responsible for flow of actions. 
* Workers Aggregate data, compute min, max and store in db, and if data is already in cache delete and update cache and commit offset
* Worker is streaming application `java/scala`. It received data  It is Spark application which never sleep. It reads data from kafka from batch each time.
* It reads 60 seconds  data point from kafka in worker, each time it gather 60 data point in a batch, then it has all necessary data needs to calculate avg, min, max, serverId, metricId
* This written into db and cache, then commit the offset. It is usefull then if worker dies and back it knows from where it needs to start. `offset is a unique identifier assigned to each message in a partition`
*  What data should we store in database? If we only need min, max it is fine to save that, otherwise we can save all 60 data in an array as heap, then to find out heapify we can get min/max 
* What happen if `data is late`? imagine some data comes late, like if the server crashed in meantime. We can design worker in a way when it reads the queue doesn't process it immediately, it can wait 10 seconds to received all data then do processing. It is called watermark period. If it didn't make it after that we can skip it
* how about `bad data`? malformed data/malicious data. If hackers hacked into machines and injected data into your system. 
* Impose structure from producer, schema validation should implement first at where data is procuded, then when it is going to be read. before puting data into kafka. Before kafka need to serialize then comprese data it means convert it to bytes which compressed data to traverse. When you read you need to first decompress and then deserialize data. Then here you do another schema validation to make sure producer and workers have same understanding of the same schemas. `kafka` knows how to use schemas
* `Schemas` should save somewhere but where? we can have a service to serve schemas call schema registry.
* `Avro` is common to validate data schemas

##### Cache
* We can only save 2 days of data in cache, it potentially is not recommended because the requirements said we want 2 days of data fast
* Problem here is how to keep data fresh?
* we can run TTL(Time To Live) eviction policy to keep it fresh `redis`, `memecache`
* `TTL` redis everything is value key. Redis will have a background job, it swip trhough cache, everything that has expired mark it and delete. 
* `Marking data` for invalidate data is good, deleting data is expensive because it needs read/write time
* `Ring Buffer`: It is a data structure, It is a circular array, everytime something come if end of the two dates, the next would overwrite the first index. It doesn't need background job
* Ring buffer live? key is string, value is string, list, hashmap. and the job of worker is design keys in a way to address ring buffer
* `Given metric Id and Time Range Queries`: How to design a cache to address such queries? we index data using serviceId, metricId, serverIdNextOn
* serviceId can save as keys. Then each serviceId has 2k metricId as object. Each metricId then has timestamp as key and value is avg,min,max values based on the time.
* user make request with serviceId and we give them all metrics needed
* user make request with serviceId and time range, it finds them and return 

##### Dashboard

* Dashboard can uses graphql, REST, grpc, settime req,  socket to get updated 
* Dashboard FE should take care of, life cycle, lb, read and write consistently, storage

* Cardinal data can be costly, cold storage after a specific of time

* Multitendancies: each organization have their own policies, so dedicate infrastructure for each specific customer. One solution is have tenand id for each. But for some small customers we can clud them togather but we have to make sure data are not mix togather.  


* create ui to handle 1000/s into queue in kafka, create topic in kafka for each one, use different instances and add sections, then consumer can read those data in order it receievs, we can send updated via socket or server sent event which needs a time interval in the backend 
* 

