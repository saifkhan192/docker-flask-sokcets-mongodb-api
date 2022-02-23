curl -L -X POST 'https://docker-flask-sokcets-mongodb.herokuapp.com/pessenger/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Saifullah Khan",
    "email": "saifkhan912@gmail.com"
}'

curl -L -X POST 'https://docker-flask-sokcets-mongodb.herokuapp.com/driver/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Sajid Khan - driver1",
    "email": "sajid@gmail.com"
}'

curl -L -X POST 'https://docker-flask-sokcets-mongodb.herokuapp.com/driver/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Ali Khan - driver2",
    "email": "ali@gmail.com"
}'

curl -L -X POST 'https://docker-flask-sokcets-mongodb.herokuapp.com/driver/register' -H 'Content-Type: application/json' --data-raw '{
    "name": "Ahsan Khan - driver3",
    "email": "ahsan@gmail.com"
}'

curl -L -X POST 'https://docker-flask-sokcets-mongodb.herokuapp.com/customer/create-trip' -H 'Content-Type: application/json' --data-raw '{
    "pessenger_id": "621646e3313ae25c8317301a",
    "pickup_lat": 31.457263,
    "pickup_long": 74.246575,
    "destination_lat": 31.534007,
    "destination_long": 74.34766
}'

curl -L -X POST 'https://docker-flask-sokcets-mongodb.herokuapp.com/customer/check-price' -H 'Content-Type: application/json' --data-raw '{
    "pessenger_id": "621646e3313ae25c8317301a",
    "pickup_lat": 31.457263,
    "pickup_long": 74.246575,
    "destination_lat": 31.457363,
    "destination_long": 74.246675
}'


curl -L -X GET 'https://docker-flask-sokcets-mongodb.herokuapp.com/pessenger/trips?pessenger_id=6215c270c460844d410a1dd4'

https://docker-flask-sokcets-mongodb.herokuapp.com/socket-frontend