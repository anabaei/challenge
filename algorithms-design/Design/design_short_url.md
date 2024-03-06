
-details- 
  <summary>  Steps to take In System Design </summary> 

1- Gather functional requirements
2- Cluster them into a collection of Microservice, assign each function related to each service and how are the requests and responses should be look like
3- Draw an architecture diagram connecting 
4- Dive into each microservice, each service should has three parts:
  - App layer: Logic of Program
  - Cache Tier: Serve popular request
  - Database Layer: Save into Disk

6 - Gather non-functional requirements:
  - Capacity requirements
  - What extend should we scale each tier  
  * Use distributed system solution, means each tier (app, cache and database) should be a distribute system or a collection of machines which work togather to the same thing which a single server is doing

* In system design need for collecting the Functional requirements for(functions that this system has to accomplish)
  * To detail out problem statement
  * To describe user's view of the system
  * To design minimum viable product
  * Convert each functional requirment to a function in server

* Monolotic is use depth-oriented approach to design
* A third party to save authentication use depth-oriented
* 
* CPU usage is Time Complexity
* RAM usage is Space Complexity
* Scalability: Build a system to handle millions of traffics comes to our system
* APIs: use for client-server interaction enabling to hide the complexities of the service
* URL: Uniform Resource Locator, includes 
  * protocol: indicate which protocol is used by client to comunicate
  * webserver: which webserver is going to hit
  * papge: which page of the webserver
    * https://www.servicename.com/page1
  * short_url: some services can created a unique short links from long urls, and map them with any URL you have  [bitley](https://bitly.com/). Also you can keep track of number of hits on your URL
    * Some medias don't allow you use long urls like twitter, or sms messages which may be limited 
    * Bitley can allow use to update url to a meaningful name
    * Marketing can track of which individual can work better for the company to encourage people to land our service
    * even we can use first half of custom domain name
    * 
</details> 

-details- 
  <summary>  Design a shortend url </summary> 

* Need to define two function requirements
  * Encode the current url
  * Decode the upcomping url and redirect to actual one
* To Encode we can have:
  * Predicted urls like below to convert to base64 any upcoming element:
```python
def base10_to_base64(num):
    # Define the base 64 alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    # Initialize the result string
    result = ''
    print("alphabet ",alphabet)
    # Convert the number to base 64
    while num > 0:
        remainder = num % 64
        print("alphabet[remainder]", alphabet[remainder])
        result = alphabet[remainder] + result
        num //= 64
    print(result)
    return result

base10_to_base64(127)
```
#### How make sure the message is not tamper on the way?
  * One is to encrypt it in a way to avoid predictable urls:
    * Any ecrypt could be duplicate key, so after creating an ecrypt first check if alreay a key exist (in O(1)) if not then assign url to this key
    * To make sure a message is not `tamper` from client to another client
```javascript
user 1 send message m, and a hashed code of that message
user 2 receieved message m, and hashed code, use hash function from message me and the out put should be same as hashed code it received.
Then it san say message are not temper.
```
##### Cryptographic Hash Functions
* Ways of hashing
```python
MD5 output fix length of 128-bit
SHA 1   output 160-bit # secure hash algorithm 1 
SHA 2
SHA 3
```
* we can convert 128 bits to base 64 to have a shorted urls,  so need to take each 6 bits as one character which ends to roughly 22 characters
```python
128 -> base64 -> 128/6 ~22 characters
```
* If we enter one url several times we get the same result, to avoid it we can concat a counter or timestamp to the end of url, so hashed of it would be enique at the end
* We can take first 36 bits and convert it to a 6 characters, but downside would be we could have more collisions
  
#### Reduce time by Offline generating  (Key Generating Service)
* We can pre-generate short urls, before getting long urls then match them togather. For this you can pregenerate short urls and put them into a queue waiting for upcoming requests.
* This way we handle duplication, we can sort it because it is offline so it won't affect the overal speed
* Downside is we need a lot of space to store it 
</details> 

-details- 
  <summary>  Scale </summary> 

#### Network Protocol
* Browser use `curl -v` command to send HTTP request under the hood of browser
*  http imply the port number is using is (80) 
* Client (browser) Make call to DNS, take response from it as Ip address of destination
  * DNS: Send names and returns IP address
* Client put Ip address of destination into header and send it
* Router Service look at header of message and look up for ip address destination
* Port numbers indicate which specific service a client needs
* Server needs to know which client ip needs to send their response and which port
```python
# request and response headers include:
ip destination, port destination, ip source, port source 
```
* Protocol: When two machines communicate with each other they need to use the same language
  * IP:specifies the format of the message as whole, otherwise the routers cannot handle the request
  * HTTP: is a protocol to get website from server

#### Web Server
* We always run multiple copies of our program as server
  * Even in system with one running program we need multiple I/O on network
  * Instead of one request waiting for I/O to complete we can use other copies of program 
* Use multiple copies of running program (multiple processors)
* I/O on webserver happen when they 

### Databases
* A server has running multiple instances of a function which accessing the same resource like database, so we call them thread (if they didn't share resources we could call them process)
* When different server accessing one database, it maybe both threads access to the same database which lead to conflict if both have the same post request -> inconsistently 
* Solution: Create a global lock, when one thread accessing resource or critical section.
  * It is lock when one thread is using it, it only gets unlock when a thread released critical section
  * DBMS (database management system) are built to handle this complexity for us

#### High Traffic
* LB is for handling traffics to servers
* If all servers were busy, need a line like bank line in front of servers, incoming request queue
* Same for response request queue if too many response comming if there were not enough bandwidth with enough data they need to be queued
  * nginx is a framework but it can act more than that like LB
  * Cache is always a subset of populare items of database to reduce the cost of reading data from db
  
#### Memory
* App service is stateless, it means it doesn't store data
* Cache layer (key,value) allows us to look up for data
* We can save or hash tables or data in RAM easily, Random Access Memory allow us to save it any where randomly in memory, but it is temporary so we need to save into Disk
* To save into Disk, we can't save it anywhere. It would be timely expensive to check Disk and find a place to save data
  * We use index to save data into database, so we have one index another value or data object
  * To get access to index, need to define a `in memory hash index` , with key values as key is the shorted url (what we look for) and key is the index of the value in Disk
    * Advantage is `in memory hash index`  is small and we can keep it in main memory
    * `in memory hash index` is located in Database layer, not in cache layer
  

### Reasons to go with Distributed Systems (6 roles) Scale Horizontally  

* less memory: DB and cache may not have enough space on a single machine to hold data with huge size -> need to split or partition data across multiple data servers
* Traffic: When number of requests coming is too much more than one tier able to handle, need to scale throughput. It means replace current server with a collection of servers
* Delay: Response time at single server is too high, then we need to parallel the work and overall time would reduce
* Failure: Single server is single point of failure, so if one is down other services can handle it
* Geolocation: If we have several servers on different locations, we minimize network latency
* Hotspots: Disporpotionally high load on a piece of data in database. In case one we split or partion data but one specific may get too much traffic, so we need to split that part as well

### More powerfull machine (Scale Vertically)
* Another solution to scale is using more power full machines
* Scale vertically means buy more power for one single machine
* If system needs to scale massively then the cost would be too high
* Working with 2 copies of machines is cheaper than one 
* Has ceiling on data size and traffic on single machine
* We can't minimize network latency 
* Single of failure still is in this

### Non Functional

* Need 3 ties in apps and 3 ties of cache to avoid single point of failure
* Need infos, like bitly creats
```bash
2 - 3 billion short urls each year 
20 billion click per month
```
* Calculate how many requests comes in per seconds
```bash
300 milion/month
10 million/day
160 k/hr
3 k/min
50 ps
-----
700 mi/day
12 mi/hr
200 k/min
3500 ps
----- 
50 or Q qps url per second is created
3500 or C ps click per seconds
read 100 more than write
But still use variable instead in case if your calulcation is wrong your answeres werent

```
</details> 

-details- 
  <summary>  Calculate Sharding or partitioning </summary> 

* 3 years is a good number for storage to keep
* The process of deviding data into multiple sections for storage is called partitioning/sharding
* Ask how many machines do we need to handle this amount of requests coming ps and how much space we need to save in memory
* In this example, if we assume we save data as key and value in hash table, value is short url and key is long url
  * How many we need to store?
    * storage space is 3 years -> roughly 1000 days
    * 24*60*60 = 86400 ~ 100,000 seconds per day
    * 100,000 * 1000 = 100 million seconds for  years
    * 10^8 * Q url created in 3 years, number of writes
    * if Q=100 -> 10 billion writes
    * Each url size max is 2048 byte,  
    * 10^10 * 2048 ~ 10^13 byte space to write

```bash
we know:
 2^30 bits-> 1 billion
 2^31 bits-> 2 billion
 2^32 bits-> 4 billion
```
* index key should cover 10 billions, so to represent 10 billions in binary we need 2^34 bits ~ 16 billion 
* each 6 bit we assign to create on char, so it is 6 byte
* 6 byte is key, 2k is the value ~ 2k byte
* 2k * 10^10 = 2 * 10^13 ~ 20 TB (trillion byte)
* if each machine store 2 TB then 
  * need to partition/shared hash tables into 10 machines
* Sharding dealing with data and managing data on different servers, it is good for heavy reads and not for write. 
* Partitioning dealing with one table, partition it into smaller portion and save to different servers, it is good for read and write
##### APPS and DB
* When we shared/partition, each server needs to access all data, so if we have 3 tier apps/cache, for each we need 10 partition
```bash
total dbs = 3 * 10 = 30 db machines
```
</details> 

-details- 
  <summary>  Calculate Cache Tier </summary> 

* Cache tier only store read data and not write data 
```bash
Uber want to hit rate of 98-99%, how much data should store in cache layer? 
20%-30%
# This is 1 role of Thumb

10% entries save into cache -> 90% read hit direct to cache
20%-30% entries save into cache -> 98%-99% hit direct to cache
```
* So if we go with 20% of 20TB key value then 4 TB save into cache 
  * Cache uses RAM
```bash
# This is 2 role of Thumb
128 GB Ram # each machine has
```
* 4 TB/ 128 GB ~ 30 partitions 
* Since we don't need any data get lost we go with 3X replicas 
  * 30 * 3 = 90 Cache machine

* How we select 20-30% to cache?
  * Sort the requests came or the most wanted short urls,
    * take top ones based on frequencies 
  * When we sort based on frequency of request, we can decide based on the data, how to manage most frequent requests on cache
  
![Cache App DB Layer](https://user-images.githubusercontent.com/7471619/224517144-37378181-15ef-4c5c-9a23-aeee4b1c280c.png)

</details> 

-details- 
  <summary>  Scale for Throughput (Handle Traffic) </summary> 

* We should know the time in ms assume `X`, is needed to process a given request by a single thread on a local single cpu to do something like i/o on that server machine
* Calculation as below shows ~ 8100 qps receive on any machine, these machine could be any server( app server / cache server / db server)
* Assume our machine has 
```bash
8-12 cores 
8 threads per core 
=> 8*12 = 96 ~ 100 threads per machine can work parallel per seconds

100 * (time on each thread 1/X) * 1000 * 30% = total time needed to process a single thread in this machine 3000/X request/sec
```
* In reality from 100 threads not all doing the process, some of do garbage collecting, some do switcing between threads, so we need only 30-40% of cpu utilization for overale health
  * because if traffic has spike then cpu has drop request,
* we have 3000/X for every machine, X is varied,for example in DB, X is more than what we have in cache or app server. 
```bash
DB Server X = 10ms , 3000 rps
Cache Server X = 2ms , 15000 rps
App Server X = 1ms , 30000 rps
```
* Now compare above numbers with 8000 rps we have in below, so our service is fine
  * Because we have 3 tier service in app layer and each one can handle traffic as 8000
  * 
* So far with design, we have
```bash
8000 qps/ query per second
73   qps / read per second
```
#### Reads
* 8000 qps hits the app service
* app service check cache for each request
* 1-2 percent of request needs to hit DB (role of thumb)
* Any request make to db, it save into cache tier
#### Write
* all reads directly hit the database and not cache

* How many service we need to handle this traffic?
  
### So Far Design Summary

* Request comes in to generate a short url (write action), 
  * LB in app server send it to a app server
  * One of threads at app server takes it
  * send request to DB
  * LB at DB guided to the right shared
  * Then thread return back result to app server
* Request comes in to get long url (read )
  * Look at Cache tier first
  * After passing from LB at Cache tier
  * Then that particulate thread returns back the url 
  * If not exist in cache tire
    * App server have to go down to db tier, to retrieve data
    * It goes through to db and return back to app server
</details> 

-details- 
  <summary>  Performance optimization (SLI) </summary> 

 service level indicators to measure the performance of a scalable system are `Correctness`,`Availability`, `(system) Throughput` and `response time` 
* Ask what type of service are we providing?
  * Then we can define the correctness of our application by data we receive from the app
  * To quantify the correct result we need Error rate to be almost zero 
They are as below
* `Correctness`: Error rate to be almost zero 
* `Availability`: Earlier we defined as a single server would be single point of failure. Calculate availability as:
  * What fraction of well formed request came in ( as specific period time) was successfully severed
```bash
if from 1000 request, one not successfully serverd 
-> %99.9 availability rate -> 3 min availability
# 3 role of Thumb 
# number of 9s are availability in minutes
99% -> 2 min
99.999% -> 5 min 
3 1/2 min -> 99.95% 
```
* `(system) Throughput`: Number of request per second that could be handle
* `Response time` The time took to return a response to the client
```bash
# studies show 300 ms or more let clients feel some delay happening
# 4 ms -> 900 ms => 25% drop of clients
```
  * Round trip request around the world could take some ms
    * Multiple data centers around the world decrease request time significantly
    * The application should have multiple servers in different locations to ensure low response time to cater to the customer services.

* Focus on decreasing response time for 99% time value
  * Median is not good, most valueable customers are longer ones
* 
 100 thread/ms, * 1000 = 10^4 
### Service Layer Objective (SLO)
* SLO is a range value of SLI's. 
* Non-Functional requirements need to explicitly displays what are 4 SLIs should be, then we can define the system
* Also `Scaling for data size`: if there is no enough space to store all data so some reponse may not even receive response, `throughputs`, `bulky system time`, `availability`, `geolocation` and `data hotspots` are meant to `SLOs`

### Service Layer Agreement (SLA)
* An explicit & implicit contract with your clients on what the SLOs should be. Including the consequences of missing SLOs. (rebate penalty)
  * If the user paid for the service and if SLOs didn't meet you assume to receive a penalty
  * For example on the span of one month the availability is 99.9%, if that missed in 1 percent get 15 days of free service
    * if you missed by 5 percent you get 45 days of free service
</details> 

-details- 
  <summary>  Latency vs Response </summary> 

* `Bandwidth` is the main ones that characterizing network performance, below we explain why:
  * There are `Bandwidth`, `Propagation Delay` and `Queueing delays`to make network latency
* Latency is duration that a request is latent (awaiting not actually service) RTT (Round Trip Time)
  * Latency is that time which request and response take to travel (RTT) between client and server on network 
```bash
Response Time = RTT + Service Time
```
* Network latency is depend on Bandwidth
* `Bandwidth` Number of bits can transmitted over network per seconds (can pure number of bits per seconds into network). It is best possible performance. The actual measure performance is called `Throughput Bandwidth`. 
* Also, we have a `Propagation Delay` which is the time takes it passes the network and is divided by distance on speed (speed of light)
* Messages are stores in the routes in middle of network, before going to the next router which is called `Queueing delays` in each router
* 
```bash
speed of light in vaccum = 3*10^8 meter/sec
speed of light in optic = 2*10^8  meter/sec
10 Mbps = 10 million bits can transmitted serially into network
-> 1 bit needs 1/10^6 time to transmit through network 
```
* Calculate `Propagation Delay` in case the server is other side of the world,  40,000 km 
```bash
circumference of the earth is 40,000 km 
40,000*1000/2*10^8 = 0.2 sec ~ 200 ms
```
* We need to add router latencies to it then it would increase
* Why `Transition Time` dominate our transmition time?
```bash
# 1 byte = 8 bits
Assume you want to download 25 MB image on 10 Mbps 
25 M * 8 / 10 = 20 sec 
```
* 20 sec is way more than 200ms we gain => Bandwidth is what dominate our response time

</details> 

-details- 
  <summary>  Reverse proxy and Forward Proxy </summary> 

* Benefits of `Reverse Proxy`
  * Increase Security
  * Add encrypt and decryption
  * Load Balancing
* LB is the public face of a `Microservice` 
* LB is single point of contact which request is send and received form clients. 
* LB is a type of reverse proxy (server side proxy)
  * Proxy: is an intermediate between the client and server
  * Reverse Proxy: act on behalf of a servers as a shield. A server side proxy that send request to internal servers
  
* When request sent from client to DNS, DNS returns the ip address of LB in APP tier.
* Client doesn't know what services are behind the LB, and doesn't need to know the ip address of each microservice.
* The entire system is hide from the public internet and only LB is the way to talk with outside
* Reverse Proxy can receive encrypted requests from client then decrypt it and send it to one of the down servers. 
  * Similarly the response can be encrypt by LB and send it to clients
  * So ip address of servers are hidden from outside organization

* `Forward Proxy` Act as web cache. or client side proxy is when we can define several clients put one Forward proxy between them and server. Forward proxy keeps a copy of all request to the server, in case duplication happen then it act like cache layer
  * `Forward Proxy` can act as a filter to ban unwanted servers access
* In fact `Forward Proxy` and `Reverse Proxy` LB talks with each other instead of client vs servers
![LB](https://user-images.githubusercontent.com/7471619/224579604-4d51a50a-c8fb-4024-9133-71248938520f.png)

* A `reverse proxy service` is a server that sits between a client and a web server, forwarding client requests to the appropriate server and returning the server's response to the client. Unlike a forward proxy, which is used to protect clients from the Internet, a reverse proxy is typically used to protect a web server from Internet traffic and provide additional functionality, such as load balancing, caching, and security features like SSL termination. By acting as an intermediary between clients and servers, a reverse proxy can improve the performance, reliability, and security of web applications

</details> 

-details-
      <summary> DNS load balance </summary>

* DNS load balancing is a technique used to distribute incoming traffic across multiple servers or data centers using the Domain Name System (DNS).

* In DNS load balancing, multiple IP addresses are associated with a single domain name, and when a client requests to connect to that domain, the DNS server returns one of the IP addresses in a round-robin fashion or based on predefined criteria such as server availability or geographic location.

</details>

-details- 
  <summary>  Load Balance </summary> 

* `Increase throughput` to our service
* LB is a software which increase throughput to the service 100-1m qps
  * Nginx is popular one
  * To distribute traffic LB uses diffrerent policies:
    * Round Robin: start from the left and go to the next one on the right and back
    * Connect to service with least connections
    * Connect to least response time
    * Random server
    * Hashing: Take one thing or number from request, and based on that decide which server should be render
    * 
* `Increase Availability`: Each server send a health check/heartbeaat to LB to tell it their availability, to remove or keep them from ones to send next request
* What if LB fail?
  * We need a passive LB. Passive LB is another single machine same as LB which share the same ip address
  * IP addresses are not hardware level they are at software level so we can do it
  *  Both LB share the same ip Address, it means both receive the request, and both health check on each other. 
  * When one is failed, then another one starting  

* DNS-based LB
    * Another solution have more than two active LBs with different ip addresses. 
    * Client relies on DNS serverice so we can define DNS service to return multiple Ip addresses to browsers.
    * The client browser take first ip address and send request to that, if one is not working then pick another one
  
* We can have both `DNS based LB` and `Passive LB` solutions.  

</details> 

-details- 
  <summary>  LB Global & Local </summary> 

* LB has two big advantages:
  * Increase throughput
  * Increase availability
  * Reduce response time (IP anycast)
* Local LB, each tier
  * Cache has a LB on top of it in cluster
  * DB has its own LB 
  * App Service has LB which exposes it to the world:
    * Local LBs help to handle throughput availability
* Global LB
  * DN base service
  * IP Anycast 

* `IP Anycast`:  IP anycast load balancing method use Dijkstra algorithm 
*  Every router knows the information about other routers in the network by broadcasting its local information
  * If we rely on round robin DNS, we can not access the closest ip address LB to the client to reduce response time
  * Solution is for each IP address that LB DNS provides, we can have several LB around the world, so same as having a passive LB, we can have several servers with same ip address
  *  We can use BFS to find shortest path to the which service we should choose with same ip, which each edge has a weight that indicate the distance. So we have an undirected weighted graph we find the shortest path from client to any source
  *  Each route get its own edges, create and adjacency list of it, use not BFS(because there is weight), Dijkstra algorithm to find closest destination ip address
</details> 
  
-details- 
  <summary>  CRUD and Compaction Process on Disk </summary> 

* CRUD operations are done on the disk
* Implement hash table storing
```bash
(k, offset on disk)
```
* where `k` key and offset on disk is the pointer to the location of the value
  * It could be challenge, on update since there may be new update needs more memory than what it had at first
  * So it is better we consider update as `deletion` and `insertion` at the end of the file
* On delete, we can only remove it from hash table, then even if it is on the disk it is unaccessible
* On update since we create a new values for the same key at the end of disk we need a garbage collector to clean up our disk
* `Compaction Process`: traverse from the end of the file and see if there are repeatation delete them to create new file create. When this completed db switched to the new one
</details> 

-details- 
  <summary>  Inconsistently, Leader & follower </summary> 

* How we can scale a DB in microservices?
* At app service layer, we scale app tier to increase availability and throughput. 
* By replacing single app server, by collection of replica app servers with a load balancer in the front. Can we do the same for the DB tier?
  * Which we have a collection of DBs behind a LB, each DB has a full copy of all data. 
  * `Data Replication`: Instead of `Service Replication` in service app layer, we have data replication. Data replication is keep copy of data on multiple machines connected over network
  * Reading from different replicas are okay
  * Writting may have issue on not syncing data in different replicas
    * Need one Master/Leader DB service, so all writting has to add to the leader and followers/slaves synced themselve with it
      * In case if one follower/leader fail, another one in reserver has to be replace

* We may have `inconsistency` in some cases when leader is not sync with all followers in fraction of seconds. But eventually there is consistently  
* Some laggs are acceptable
  * One way to optimize inconsistency, is check who is gonna read this data, if it is the same person who did changes, then send his requests only to the leader/master DB.
  * Another solution to avoid lagging is when one write come in to master/leader, lock any request on this key value request to all followers/slaves until write is completed and all followeres are sync to get all consistent respond. 
    * It means throughput would be lower, so if want high throughput we have to compromise eventual consistently
  
### MultiLeader and follower
* We can have multi leader on each region. 
* Each leader is responsible to update followers and broadcast the changes to other cluster leader to update that followers to.
* If two request came in at the same time on different leaders, each one has a UTC (universal time coordinator) then the older one wins conflict and overcome other changes when broadcasting. The receiver leader never changed any data which is older than recent changes.

</details> 


-details- 
  <summary>  Leaderless Data Replication and quorums W & R </summary> 

* We can use democracy
  * Write is done on all replicas
    * When more machines has the same data, we update minority with the data
      * If they are equal we can check the time stamp to know which one should be majority
      * We need at least one machine returns read/write request to validate the rest of replicas
      * This one makes write fast but Read is slow, because we need to read from different replicas to validate the data
      * In the middle of read, maybe only one write has done before syncing with rest, then read can get majority which is old version, so there is inconsistently

* We can have different setups for this design
```bash
# minimize read faster and write slow
Number of nodes = 3
Read only from 1 
Write into 3 machines 
# minimize write faster and read slow
Number of nodes = 3
Read only from 3 
Write into 1 machines 

# normal setup, this one can tolerate one fail on each machines
Number of nodes = 3
Read only from 2
Write into 2 machines 
```
* In a leaderless network with 7 nodes, the write `quorum` is 4. From how many replicas should we read in order to figure out what the true value is? answer is 4
* While designing a network with 15 nodes, you need to decide the values of W and R for the network. You want the network to read fast and also be fault-tolerant. Which of the following values could be a possible suitable combination for such a network? answer is W=11, R=5

</details> 

-details- 
  <summary>  CAP Theorem </summary> 

* On distributed systems we can choose Availability or Consistently, based on our design. This is called CAP theorem
*  ![CAP](https://user-images.githubusercontent.com/7471619/226084940-7e792639-65df-4a36-b92d-ee1ce40bd35f.png)
</details> 


-details- 
  <summary>  CDNs </summary> 

* By having different data center around the world
  * Reduce response time
  * Increase availability 
  * Increase throughput 

* Usually `number of Reads req  >> number of Writes req` so we can focus on `Read` to optimize it
* To optimize response time to `Write` we could have replicate of databases around the world with multiple `master` node in each one
* To optimze `Read` we don't need a datacenter in each region
  * If the app tier is not complicated we can have whole as a app and cache in other regions
  * It is called `proxy cache` 
  * Since this proxy cache is close to region of client, the response time is short
* ISP become overwhelms with uploading huge files with traffics since each file needs to cross files 
  * If we transfer files in proxy cache in advance, then it would have less traffic on our network
* This is the Idea of `CDN`s
### CDN (proxy cache on the server side)
* Is a good way to reduce response time and increase availability without building new data centers
* Content Delivery Networks: is geographically collection of proxy caches which stores most of populare requests
  * It is a replicas of master servers geographically distributed services
  * Static content, not dynamic content like stock prices can't be like that
  * Netflix Amazon have it's own CDNs servers. 
  * Youtube videos can be sent to their own ISPs which have CDNs

* CloudFlare and Akamai are third party distributed network to keep your data 
* Part of pages can comes from database service and the rest could use the ip address of the client and cloud flare can decide which CDNs can send static file from the geographically closes
* 

* Content Delivery Network is a popular way to replicate our data to reduce response time improve availability and throughput without needing to build multiple data centers.
* Third party CDNs like Cloudflare and Akamai can be used for that
* 
* At above image, we can remove on DB in one region, and send all read and write to one DB. It would be still fast
  
*  To optimize Write, we end up to have multiple leaders in each region 
* Also there is browser caching on each client
* Forwarded proxy can help caching requests comming from one organization, but no body outside of that organization not benefit from that
* Network can be congested if we use other region DB for reading for big files like movies, the bandwidth would be issue
* 
</details> 
-details- 
  <summary> Cache Read and Write  </summary> 

* CDNs helps availability and throughput
```bash
# calculate throughputs on each section on each thread
# server gets 30,000 rps 
# cache repose is 2 ms, db response is 10 ms
=> cache 15000 rps
=> db 3000 rps
```
* Porpuse of cache tier is improve read 

### Read
* v = get(x)
* if v is null then cache missed 
  * check db
  * put it into cache


* Main purpose of cache tier is increase throughput
* Save every request in cache, but it may get full
  * In order to make space for new key value pairs in cache, we need to delete the current ones
  * There are different cache eviction:
    * Random removing pairs from memory
    * LRU policy (Least Recently Used): throw out the 


</details>

<details>
  <summary> Least Recently Used LRU </summary> 

* Implement get(key) to check cache  and  put(key, value) to put key value pair in cache in O(1)
* We save key values into hash table
* 3 Common ways to coquire data:
* `Balance Tree like Heap` -> takes logn, 
* `Hash tables` -> have no ordering 
* `pre sorting` -> it is sort
  * `pre sorting` allows us to put most recent in first index and get the one that should be deleted from the last item in `it`
  * so even we don't need to keep timestamp 

* `it` can't be an array because we want constant time when we insert at the front of the array, so we chose a linked list. A dwal linked list which tailer linked list which has two pointer to tail and front nodes

* 


</details>