curl -L -X POST 'http://localhost/pessenger/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Saifullah Khan",
    "email": "saifkhan912@gmail.com"
}'

curl -L -X POST 'http://localhost/driver/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Sajid Khan - driver1",
    "email": "sajid@gmail.com"
}'

curl -L -X POST 'http://localhost/driver/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Ali Khan - driver2",
    "email": "ali@gmail.com"
}'

curl -L -X POST 'http://localhost/driver/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Ahsan Khan - driver3",
    "email": "ahsan@gmail.com"
}'

curl -L -X POST 'http://localhost/customer/create-trip' -H 'Content-Type: application/json' --data-raw '{
    "pessenger_id": "6215b0bc76fa8a123b984020",
    "pickup_lat": 31.457263,
    "pickup_long": 74.246575,
    "destination_lat": 31.534007,
    "destination_long": 74.34766
}'

curl -L -X POST 'http://localhost/customer/check-price' -H 'Content-Type: application/json' --data-raw '{
    "pessenger_id": "6215b0bc76fa8a123b984020",
    "pickup_lat": 31.457263,
    "pickup_long": 74.246575,
    "destination_lat": 31.457363,
    "destination_long": 74.246675
}'


curl -L -X GET 'http://localhost/pessenger/trips?pessenger_id=6215c270c460844d410a1dd4' --data-raw ''

http://localhost/socket-frontend