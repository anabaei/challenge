
### API
* API is Application Programming Interface
* API is specification of possible interactions with an application
  * `External API` (open API):Public API which can be used by any developer
  * `Internal API` is internal communication between modules, 

* What is REST: 
 REST is an architectural style for designing networked applications. It is Client-Server Architecture, Stateless, HTTP Methods 
 * 
#### Examples:
* `https` example like common way 
* Objects like what `AWS Python API` provides:
```
pip install boto3[crt]
or
pip install boto3
aws configure // located at s ~/.aws/credentials
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
``
```python
import boto3
# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)

s3_client = boto3.client('s3')
response = s3_client.upload_file(filename, bucket, objname)
```

### SOAP
* XML based communication protocol between services. Mostly used to implement RPC pattern
* Transport agnostic is http and smtp
* Invoke services in RPC (Remote Procedure Code) style
* Uses WSDL web service descriptive language to define services, to define messaging formats
* If you missed the format of the message you get error
### REST
* Architecture style that defines how to access resources in  distributed systems. There are six features in REST
  * Uniform Interface
  * Client-server model -> use uri to get 
  * Stateless -> server never store any data
  * Cache -> resources are cacheable on client and server
  * Layered architecture 
### RESTFUL API
* Resource based API design approach in REST systems

* session afinity: allows you always stick to the same node server, (this sessioning requests, break distributed design because we force request to a specific node al the time )
* gRPC, GraphQL, REST
* paradigm == model, philosophy , notion = idea
* micro frontend architecture
* `POST` creates a new resource. Even if there is same item, it create new row with different id. `PUT` replaces a resource everytime you run. `PATCH` has structure how to change resource. 
* `Put` works as `POST` if user not exist
* `HTTP 409` conflict already existed on several post 
* `Patch` If the client sends data with an identifier, then we will check whether that identifier exists. If the identifier exists, we will update the resource with the data, else we will throw an exception.
Note: On the PUT method, we are not throwing an exception if an identifier is not found. But in the PATCH method, we are throwing an exception if the identifier is not found

### Pagination
* If there are millions of records on each requests you need pagination
  * One solution is sending a token
  * One is sending, you don't need to travers all, you can skip many pages as
  ```
  "current_page": 1
  "request_per_page": 100
  "total_result": 250

  ```
  * One solution is HEATONS 
### Current path
```
/parent/:id/children
```
* Nested is not acceptable
```
api/users/:user_ud/posts/:post_id/comments/:comment_id
```
Instead of `uri parameters` use `request parametes` seperate by `?` as
```
user/comments?user_id=123 -> give me all the coomments for this user
user/comments?post_id=123 -> give me all the posts for this user
user/comments?comment_id=123 -> give me all comments for this comment
```
## Some Rules
* use kebab case, not camelcase 
```
.../creation-date 
```
* prefer lower cases
* don't include trailing slash (last slash)
  
## Secure API 
* Never put api key in URI
* USE Https
* Use OAuth vs basic auth
* Add timestamp into API key
* Enable timeout, rate limitation and throttling
* Validated input params

## Document API
* Write example input and output
* openAPI or Swagger 

## API Security




## Design APIs
### Define resources first & define endpoint (means add action verbs)

* REST API get data directly from db, which we call it resources
  * First define resources then define endpoints
  ```
  /shopingt-cards
  {
    "id":
    items: [ -> subresource is item
      item_id: 
      price:   -> not exist in post only in get
      quantity: 
      tax: -> not exist in post only in get
    ],
    lastUpdateTimestamp:
  }
  ```
  * Don't get lost in small issues, because you waste too much time at beginning and let interviewer get into details 
  * Add shipping id to JWT, then you can always access to your shoppings carts not others
  ```
  GET /shopingcarts/{id}
  GET /shopingcart -> return all shopping carts for me
  POST /shopingcart
  to update there are 4 solutions:
  1- PATCH /shopongcart -> pass partial of items you want to  change
  2- PUT  /shopongcart -> pass all the items, because it overwrite
  3- POST  /shopongcart/modifyCart ->
                    {
                      "action": "add/remove"
                    }
  4- hit the sub resource directly
     POST /shopingcart/items/:item_id
     DELETE /shopingcart/items/:item_id
     * you can ask because we can have post/delete vs put here
     PUT /shopingcart/items/:item_id
  ``` 
  * Request header usually is the one authenticate you.
  * Pass epoc time helps vs UTC.
  * It is important who is calling this API, for times. 



  *  
  
  #### CacheAbility is core of RESTful API



### Scrum
* Scrum is an agile framework for developing complex projects, includes:
  * `Sprint planning`, `Daily Scrum`, `Sprint Review`, `Sprint Retroperspective` 

