# General System Design

* 3 main pattern of Designs to fix problem, k-v and streaming analytic are most commons.
  ![batch](https://private-user-images.githubusercontent.com/7471619/268524877-be37612f-7558-4d3f-8149-8253f1ee6810.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ5ODUxOTAsIm5iZiI6MTY5NDk4NDg5MCwicGF0aCI6Ii83NDcxNjE5LzI2ODUyNDg3Ny1iZTM3NjEyZi03NTU4LTRkM2YtODE0OS04MjUzZjFlZTY4MTAucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMDkxNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzA5MTdUMjEwODEwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZmRkYTQ3NjI1ZDdiNzlmNjQzMzY2YzBlNmQyZTIxYjQ0NDYyNjAzYzNiY2Y3OTU2OGU2ZmJiNzYyMTJkMTY0ZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.8WSn1c_kHeJ5jg9LYqMzvCHXoCMWhtXJDlBnehmvGOc)
* Online CRUD Design
* New Realtime design (streaming): When we want to measure a service like your homes security cameras, temprature online and you need instance analytical. If we want to analyse data with complex algorithms so it would be in next category
* Compute Intensive design (mostly read only)
  

#### Step 1: (product manager)

**

* More changes require 
* APIs Questions:
* How large is data record?
* How many data record to handle?
* What would be response time of the API? 
* How many API Calls per second
* Consistently over Availability, which one is more important here?

* Generic non functional requirements (these are very low level engineering, we just list them and later use), most of them are yes usually but it is good to ask
* Availability
* Reliability
* Hotspots
* Geo 
* Security, rest encrypted, ssl


#### Step 2: (Engineer Lead)
* Engineer lead should devide into components and assign each one to a team. Here is the concept of Microservices come in. You devide application into services where each component is independently maintainable and testable, loosely couple, independently deployable, organize around function requirements and can be owned by small team


* For example: Profile, messaging, notification in Linkedin are seprate teams(services), Messaging and profile have the same apis, but handle with two different teams. 4 APIS for Profile(CRUD) and 4 for messaging require. At `linkedin` there are `4` different teams:
    * The team `identity` handle profile use cases
    * The team `feed` handle feed 
    * The team `messaging` handle messaging use cases   
    * The team `notification` handle notification

* `Netflix`
  * The team for `content delivery`
  * The team for `user accounts`
  * The team for `payments`
  * The team for `feed/recomendations` 

* If `data model` are different, the belong to different services 
like profile and messaging in linkedin
* If `data model` is same but api are different so services are different

- At this step you know your interview is deep though breath through
- If you become to one, two buckets( services) you are in depth design, but if you comes with 5,6 services you are in breath design

#### Step 3: Propose Umberella Architecture 
* As VP of engineering,  Propose how microservices interact with each other and client
* Write the pipe lines and flows between blocks (breath first through)
* `Rules of Thumb`:
  * if high volume data (in size of less than 100kb), needs to push in real time between microservices, use publisher/subscriber
  * Any async comunication between microserves use pub/sub
  * Pub/sub is microserivce thing
  * To pull data from server use REST API
  * If data tansfer is offline use batched ETL

#### Step 4: Delegate Design of Building Block
* Here is where engineering comes in picture, to deep dive each component, If too many services you may choose one or two to dive deep
* For example, at netflix design system `recomendation team` makes most important role in compnay, you may take it
* 

Budget 
![batch](https://private-user-images.githubusercontent.com/7471619/268528304-c68beb7d-9c41-41b2-bffa-50265bc4ecf3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ5ODUwOTQsIm5iZiI6MTY5NDk4NDc5NCwicGF0aCI6Ii83NDcxNjE5LzI2ODUyODMwNC1jNjhiZWI3ZC05YzQxLTQxYjItYmZmYS01MDI2NWJjNGVjZjMucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMDkxNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzA5MTdUMjEwNjM0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZGMxNDJiMmM1ZTQzNGI1MjI3ZWE2MjhmNDc4NDU0NjkwODE3YmM1ZWYzY2E2YmQ1NzNkYjkyNDNjNDE5MzIwOSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.TN51tE4zvUX49SSP97RUmwelXv4M1FR_D3sqC5JrdWU)

* If it is `Breath Oriented`, if APIs are clear by interviwer then need to spend 2-3 min to clarifing and asking questions, then spend time on bucketizing, umberella architecture then delegate dive deep services

* If it is `Depth Oriented` means only one or two component you need to talk (online reserve), APIs are clear so only spend time 1-2 minutes on  clarifying quesitons, no time on bucketing, no need to umberella and no need to delegate or priotize, because there is only `one main` service. So directly go to `deep dive` technical  

* As a product manager usually expected breath, but as software engineer it is expected depth.
* 


* To eveluate performance we consider 3 parts:
* `Response Time`: Server Processing time + time spent on network trip to server and back: `300ms` is good, more than `1s` is bad
* `Availability`:
* `Throughput`: 




### Batch System Design 
* Problem
![search](https://private-user-images.githubusercontent.com/7471619/268529264-8e730a7e-95c4-4b3b-9b08-a92853830cbe.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ5ODY2MDksIm5iZiI6MTY5NDk4NjMwOSwicGF0aCI6Ii83NDcxNjE5LzI2ODUyOTI2NC04ZTczMGE3ZS05NWM0LTRiM2ItOWIwOC1hOTI4NTM4MzBjYmUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMDkxNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzA5MTdUMjEzMTQ5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MzY3YmQxYmU5NmE3Y2M1Njg5ZGMwZGE3Y2Q0ZmY5MTYyM2Y1NWYzNWIwZDdjMzVhY2FmYzc5MjQ5NWVhNDUxNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.qKMbwQjBdcytttbvMu8TBXxcJUvGQnJ_z87HL5klkaY)
* From above, the second to last bullet points are the ones which you had to ask interviewer if there weren't mentioned, so here APIs is clarified so only needs to spend `1-2` minutes 
* Above it asked to design `just one` the search API. so the following questions should be asked. IF there are 10 APIs `don't` ask NFR for each API. 
  * What would be response time of the API? fast
  * How manay calls per/seconds? google has 100,000/seconds
  * Consistently/availability? here is always `available` 

* `Preprosessor` here means web crawlers which has done their jobs. 
* `static pages` means pages are statics only
##### NFRs
* Ask generic NFRs like:
 * Should the system be `available`?
 * Should the system be `reliable` ?
 * Should the system handle `hotstops`? it means if a loft of request call a service and cause perfomance issue. 
 * Should the system be `Geo` distributed system ? the answer is `no`
 * Should be secure? yes
 * Because it is deep dive, so it skip step 2, 3 and dive deep into 4
### Design building block
* Compute intensive has two tier: `compute app` and `storage`
* `App tier` is our web service, 
* `In memory` compute tier which we create our code here, we don't need cache here since `compute engine` works as cach, 
* `Hitting storage` takes 5,4 times more in hitting cache, and storage is more expensive to scale, and to protect data storage
* `reverse index`: index usually is a key to give you document, but reverse index you give document to get which index or id of web is relevant to it. Here in case of term: webId, is called that
* For example, netflix search:
```
Term: sorted List of content Ids
```
* `Yel` search
```
Term: sorted List of bissiness Ids
```
* `Amazon` search
```
Term: sorted List of product IDs
```
* This is how elastic search save data and do the `search`, elastic search throw whatever garbage is in the term and implement search based on the rest
* `Data Strucutre`:  save it as `Hash Map`
* `2:37`


* Some brand names 
![brandnames](https://private-user-images.githubusercontent.com/7471619/268531641-fccd51b2-c24c-421e-b6bb-97cd2c7590cb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ5OTAyOTgsIm5iZiI6MTY5NDk4OTk5OCwicGF0aCI6Ii83NDcxNjE5LzI2ODUzMTY0MS1mY2NkNTFiMi1jMjRjLTQyMWUtYjZiYi05N2NkMmM3NTkwY2IucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMDkxNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzA5MTdUMjIzMzE4WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YmQ1MzRlYjM5NTg5NzRmM2UxZjg5ZTY0YzRhZTE5Zjg0MTQxNzA0Yzk5ZmRiOWE5NDY1ZTJhN2FhODkyM2I1YiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.7NxNKxErdfJexZk0hVjPDaAhcqyu1c2E3cqzqRvxQIY)
* 