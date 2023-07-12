#!/bin/bash

curl http://localhost:5000/api/timeline_post # Get the current posts
curl -X POST http://localhost:5000/api/timeline_post -d 'name=test&email=test@email.com&content=Testing' # Add a testing post
curl -X GET http://localhost:5000/api/timeline_post # Check if the post was added correctly
curl -X DELETE http://localhost:5000/api/timeline_post -d 'id=test' # Delte the testing post
curl -X GET http://localhost:5000/api/timeline_post # Finally, retrieve one more time all the post
