#!/bin/bash

# create topic
curl localhost:5000/topic/topic1 -X POST

# subscribe 1 user
curl localhost:5000/subscription/topic1 -X POST

# publish a message
for i in {1..500} 
do
    curl localhost:5000/publish/topic1 -H "Content-Type: application/json" -X POST -d @requests/1kb.json
done

# retrieve the message
for i in {1..500} 
do
    curl localhost:5000/subscription/topic1/0 -X GET
done
