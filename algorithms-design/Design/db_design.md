# System Design
* Need to at least mention nonfunctional but usualy 
focuse on functional 

## Functional Requriements 
* 

## Non Functional Requirements 

* Scalability
* Accessability special for people with disability
* Security


## Checklist 
* Understand requirements (important):  
* Critical thinking: Identify problems, use cases, cost and reliability
* Articulate Thinking: Show and support your design to your coworkers. Pay attention to suggestions
* Technical Knowledge: Know what you talking about, don't bring topics you don't understand
* Fault Tolerate: Make sure edge cases failor, internal external faulors, how to test
* Scaleable: 
  * Volume usages: proper number of node, lbs
  * Schema type, take db matches your development
    * if there is constraint and stop using you delete them use nosql, specially in data migrations
* Save Costs


### Databases for:
* Transactions
* Search
* Low-latency
* Long term storage
* Ephemeral Storage
* Time Series 
* The cloud
* On Premises
* Analytics
* Grouping
* Big data 

## Scale ability
* Read Heavy -> caching helping


### OLTP
* Order and payments from customers as structure data in RBMS 
* Put customer satisfaction survey through online that represent unstructured data in S3 cloud blob file storage 

### OLAP
* Online Analytical Problems provide business intelligence to generate reports uses by product managers
* such result can determine future business strategies 
* Only big companies when need analytical data in case of cost

## ETF process To construct complex queries 

* Aggregate data (select rows you want)-> Normalize(convert to usd)-> Data Warehouse 
* ETL Tools
  * You can use node.js 
  * Some are enterprises like Apache is open source, Informatica and talented are not free

## Data Warehouse
* 
* Amazon Redshift
* Snowflake
* Greenplum 
* Teradata


### Star Schema
* Keep it small
* one join 
  * easy 
  * fast
  * duplication and redundancies
  * hard to migrate since many rows should be updated


## Normalization

* Remove redundancies
* Get benefit of joining tables
* 

### First Normal Form
* All Rows in all tables must be unique
* Each Cell must contain a single value
* Each value should be non divesble (can't be slip down further)

### Second Normal Form
* It is based one First one
* No partial dependency -> All non prime attribute must depend on candidate key (not a partial of candidate key)
  * Student id, course id -> it is a composite key -> course fee depends on only course id and not student id -> non key course fee depends on partial of composite key -> which is violate second normal form -> the problem here is when you change course id then you can't change all courses fees associate -> only if each students could pay different price based on their credits then this table is good -> we can break it into two table, one student id course id and another course ifd and price
  
### Third Normal Form
* No transitive dependency -> All attributes must only be determine by the primay or composite key and not by the other keys
  * Example is tournament table with winners and the year, composite key is routnamnt name and the year, Date of the birth attribute is related to winner id, which winner id is not primary here so it is violation


column (attribute) Rows (data)

## Index
* Is a way to get data faster 
* Can ensure uniqueness on each 
* Cluster Index:
  * Store data in which data is created 
  * Select covers most of columns of table
  * RDBMS take primary key as index if we don't specify
  * 

* Non-Cluster Index
  * When quering on clumns that not in primary, if cetatin columns are always query and 

* ColumnStore Index
  * Data store in clumns not rows, it uses heavy comprehension and save money less memory, get to information faster -> 

* Issues of Index:
  * Take additional space
  * Useful for reads not useful for insert, 
  * Order by clauses that are not clouster index, index are not helpful
  * If you have too many index it makes is very easy
  * Reads fast, write slow -> turn off indexes special for bulk data migrations

### Partion
* Is a way to manage large range of data
* Move certain columns less use to other tables
* Comlumnstore index can save 30% of memory but will be slower to get query

### Transactions
* Atomic - all or nothing
* Consistant - maintane database even if db is down
* Increase availablity on more than different places in case of down a server
* https://www.sql-practice.com/



### Union
select name form Patient as 


## Database Query Performance Optimization 

* Add cluster and non cluster index for faster reads
* Remove exesive index for faster write
* Reorder joins (small tables to left)
* Query on filtered data set not the entire table
* Use temp table CTE for storing  filtered data
* Return minimal set of clumns 
* Caching data
* Shard database / users eg along geographical lines
  * Sharding is a process of dividing database into smaller unit keys
  * Difference with partioning is partitioning is the same table but shard make two different table from one
  * Some dbs have shard capabilities
  * different users in your system, one database holds customers and advertises users as cutomer. If you design linkedin, you connect with your region ppl, you could shard based on your region ppl, cross region association is less common
  * Add more machines to laod 
  * Seperate a table into two tables, 
  * shard is in app level
  * It is complex, make your app level complex, it could be unbalance shard 
* Partiitoining move old data to cold storage
* Separate read replica/ cache for non transactional data and reads


## DB in Cloud
* 