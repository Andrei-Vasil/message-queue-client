#!/bin/bash
for i in {1..5000}
do
   curl "localhost:5000/push" -X POST -H "Content-Type: application/json; charset=utf-8" --data @data.json
   curl "localhost:5000/pop" -X GET
done
