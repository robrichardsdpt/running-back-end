#!/bin/bash

curl "http://localhost:8000/runs" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "run": {
      "date": "'"${DATE}"'",
      "time": "'"${TIME}"'",
      "distance": "'"${DISTANCE}"'",
      "location": "'"${LOCATION}"'",
      "RPE": "'"${RPE}"'",
      "notes": "'"${NOTES}"'"
    }
  }'

echo
