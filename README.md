
# Docker, Flask, MongoDB, Sockets API
[![Author](http://img.shields.io/badge/author-@saifkhan192-blue.svg)](https://www.linkedin.com/in/saifullah-khan-02318086/)

A Simple project that uses Docker, Flask, MongoDB, Sockets

## Features

-   Todo: Authentication Layer
-   Todo: Add modules for Models, Repositories, Services etc
-   Todo: Exception handling
-   Todo: Use Redis for caching
-   Todo: Use Marshmallow Schemas for response building for apps


## Project  structure
```sh
│   ├── direction_service.py
│   ├── exceptions.py
│   ├── flask_app.py
│   ├── flask_app.pyc
│   ├── fontend_app.py
│   ├── geo_helper.py
│   ├── helper.py
│   ├── __init__.py
│   ├── models.py
│   ├── mongo_helper.py
│   ├── repositories.py
│   ├── run_server.py
│   ├── tests
│   │   ├── config.py
│   │   ├── conftest.py
│   │   └── test_trip.py
│   └── wsgi.py
├── ccurl.md
├── docker
│   ├── bash_history.log
│   ├── docker-compose.yml
│   ├── DockerfileApp
├── gunicorn_starter.sh
├── Makefile
├── Procfile
├── pytest.ini
├── README.md
├── requirements.txt
├── runtime.txt
├── static
└── templates
    └── socker-client-page.html

```

## Getting started

```make
git clone https://github.com/saifkhan192/docker-flask-sokcets-mongodb-api.git
cd docker-flask-sokcets-mongodb-api
make build && make run_app
```



## Deployed on Heroku

Link for Home page:
https://docker-flask-sokcets-mongodb.herokuapp.com/

Link for Socket Demo Page:
https://docker-flask-sokcets-mongodb.herokuapp.com/socket-frontend


## Tests
### Running  Test Cases

```bash
make run_tests
```

## Usefull Make Commands

```make
make follow_logs #show flask debug output
make bash_app #ssh into the app
make refresh_app #recreate app if flask does not reload on files changes
```
