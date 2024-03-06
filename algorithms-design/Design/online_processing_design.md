
# General System Design

![system](https://private-user-images.githubusercontent.com/7471619/268533474-e1b044de-91d3-43a9-a26a-dbb82fef4e3d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ5OTI4NzUsIm5iZiI6MTY5NDk5MjU3NSwicGF0aCI6Ii83NDcxNjE5LzI2ODUzMzQ3NC1lMWIwNDRkZS05MWQzLTQzYTktYTI2YS1kYmI4MmZlZjRlM2QucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMDkxNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzA5MTdUMjMxNjE1WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MDNkYWZhMGE1Y2M3YTUzYTgzNTliMzRjNzM3MzIwMjJjMjNkYTc0OGIzY2Y4NDdmYzA5OWMzNzZiYzZmYzQ3MSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.ugRjNps1lBBJG_QrvZrPlYh4Q3wUMQgZ6VMFgGl8CFw)

* If user needs response then use REST API, if no need to response then use pub/sub
* 


## Online Processing Instageram

* Gather Requirements:
  * View
  * Upload
  * generate feed
  * follow/unfollow
  * user management
  * Like/commnet photos
* Available -> yes prefer availability over consistently
* Reliable -> no lost photos
* Accept latency X in view feeds

* Total users: 1billion
* Daily active users: 500 million
* New photo per second: 1000
* Photos views per second: 20000
* Average photo size: 200kb


### Step 2:
* User should be able to view or upload photos:
  * viewPhoto(photo_id, user_id)
  * viewPhoto(user_id)
  * postPhoto(user_id, location, time_stamp, title, tags[])
* User should be able to like/comment
  * likePhoto(photo_id, user_id)
  * postComment(photo_id,user_id,time_stamp, comment)
* User follow/unfollow
  * follow(follower_id, followee_id, time_stamp)
  * unfollow(follower_id, followee_id, time_stamp)

* PhotoTable, UserTable, LikeTable and CommentTable are require
* Define microservices
![micro](https://private-user-images.githubusercontent.com/7471619/268534246-5785721f-7ce5-4910-bfb2-f8f275dfab95.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ5OTQwOTAsIm5iZiI6MTY5NDk5Mzc5MCwicGF0aCI6Ii83NDcxNjE5LzI2ODUzNDI0Ni01Nzg1NzIxZi03Y2U1LTQ5MTAtYmZiMi1mOGYyNzVkZmFiOTUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMDkxNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzA5MTdUMjMzNjMwWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NDYxMjY2YjQyMGExODEwNDExY2NmODIwOTlmOTgyODMzMTY4ZjVkOTcwZDM4MzJiNTU4MmE2YTg1YjJkY2MwOSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.ZliGBOB7IQCydlMSICs7yo-veOK4dtU2GvzW8Ki5-Q0)
* viewService and postService could be same or different

### Step 3:
* `View a Photo` If you see a photo from viewSrv, it needs to get data from likeSrv and commentSrv then pass it to the client
* `Post a photo` if you post a photo your friends may not need to see it write a way, so it would first save it into DB then make request to fanout service which provide feeds for your freinds, and save into reverseIndex for `search service`.

* it should take only `2 min`

![link](https://private-user-images.githubusercontent.com/7471619/268534490-f1d527af-6ac1-497f-9230-3d09b5b88cee.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTQ5OTQ0ODYsIm5iZiI6MTY5NDk5NDE4NiwicGF0aCI6Ii83NDcxNjE5LzI2ODUzNDQ5MC1mMWQ1MjdhZi02YWMxLTQ5N2YtOTIzMC0zZDA5YjViODhjZWUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMDkxNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzA5MTdUMjM0MzA2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODM1MDFlYjA0MDM4OWEwMjBmMWY1YWNhNGEwZmRjYmRiZTI3ODZmMTc3NzE0N2NjZjFiZjE0NDljZmIxYjU5YSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.QOP_Ncg7amvGfZHl6eYfqKQOX4UXREGtcb0nIQ6QEyI)

* 1.45 sanjay online

