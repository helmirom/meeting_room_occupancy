# Meeting Room Occupancy
Version : V3

### Task Goal :

The main goal of this task, is to implement an API to calculate meeting rooms occupancy.

### Specification
The API must include 3 routes :

1. **Webhook**

Allows sensors to publish data about IN/OUT count of persons.

Endpoint :
```
http://hostname/api/webhook
```

Request Example :

```
curl --header "Content-Type: application/json" \
        --request POST --data \
        '{"sensor":"abc","ts":"2018-11-14T13:34:49Z","in_count":3,"out":2}' \
        http://hostname/api/webhook
```

2. **Users**

Allows third party applications, through a GET request to get sensors list.

Endpoint :
```
http://hostname/api/sensors
```

Request Example :

```
curl --request GET http://hostname/api/sensors
```

Response Example :

```
{
    "sensors": [
        "abcd"
    ]
}
```

3. **Occupancy**

Allows third party applications, through a GET request to get occupancy on a specific room.

Endpoint :
```
http://hostname/api/sensors/<sensor>/occupancy
```

Request Example :

```
curl --request GET http://hostname/api/sensors/abc/occupancy
```

Response Example :

```
{
    "inside": 3,
    "sensor": "abcd"
}
```

**_Optionnaly:_** 

4. **Occupancy at a given instant**

Allows third party applications, through a GET request to get occupancy on a specific room at a specific instant.

Endpoint :
```
http://hostname/sensors/<sensor>/occupancy?atInstant=<instant>
```

Request Example :

```
curl --request GET
http://hostname/sensors/abc/occupancy?atInstant=2018-11-14T14:00:00Z
```

Response Example :

```
{
    "inside": 3
}
```

### Implementation

At this version of implementation, the solution integrates 3 docker containers : API, PostgeSQL, Frontend

**API container**

The Stack mainly is Python with  version :
```
Python 3.8.10

```

This implementation uses fastApi framework 
```
Name: fastapi
Version: 0.75.0
```

**Main app tree**

The app is composed of those layers:
```
.
app
├── api
│   ├── crud.py
│   └── __init__.py
├── db
│   ├── database.py
│   └── __init__.py
├── __init__.py
├── main.py
└── models
    ├── __init__.py
    ├── models.py
    └── schemas.py


```
**Database **
**Tests tree**

Implemented tests covers unit, functional tests and __Postman__ collection used to test the API.
```
tests
├── conftest.py
├── functional
│   ├── functional_scenario_test.py
│   └── __init__.py
├── __init__.py
├── postman
│   ├── __init__.py
│   └── mro_api_test.postman_collection.json
└── unit
    ├── api_is_up_test.py
    ├── get_sensors_list_test.py
    ├── __init__.py
    ├── occupancy_at_instant_nok_test.py
    ├── occupancy_at_instant_ok_test.py
    ├── occupancy_nok_test.py
    ├── occupancy_ok_test.py
    ├── webhook_query_nok_test.py
    └── webhook_query_ok_test.py
```

### Usage
**Running Stack**

Create a __virtual env__ using :
```shell
$ docker-compose down && docker-compose up --build -d && docker-compose exec api python -m pytest

```

By default, the app will run on :
>API : localhost:80
>Frontend : 8080


```shell
web-db_1  | PostgreSQL init process complete; ready for start up.
web-db_1  | 
web-db_1  | 2022-03-28 15:08:21.688 UTC [1] LOG:  starting PostgreSQL 14.2 on x86_64-pc-linux-musl, compiled by gcc (Alpine 10.3.1_git20211027) 10.3.1 20211027, 64-bit
web-db_1  | 2022-03-28 15:08:21.689 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
web-db_1  | 2022-03-28 15:08:21.689 UTC [1] LOG:  listening on IPv6 address "::", port 5432
web-db_1  | 2022-03-28 15:08:21.691 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
web-db_1  | 2022-03-28 15:08:21.694 UTC [50] LOG:  database system was shut down at 2022-03-28 15:08:21 UTC
web-db_1  | 2022-03-28 15:08:21.698 UTC [1] LOG:  database system is ready to accept connections
api_1     | PostgreSQL started
api_1     | INFO:     Will watch for changes in these directories: ['/usr/src/app']
api_1     | INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
api_1     | INFO:     Started reloader process [1] using statreload
api_1     | postgresql://postgres:postgres@web-db:5432/web_dev
web_1     | 
web_1     |   You can now view your Streamlit app in your browser.
web_1     | 
web_1     |   Network URL: http://192.168.240.4:8080
web_1     |   External URL: http://176.160.198.33:8080
web_1     | 
api_1     | INFO:     Started server process [32]
api_1     | INFO:     Waiting for application startup.
api_1     | INFO:     Application startup complete.
api_1     | INFO:     192.168.240.4:51516 - "GET /api/sensors HTTP/1.1" 307 Temporary Redirect
api_1     | INFO:     192.168.240.4:51516 - "GET /api/sensors/ HTTP/1.1" 200 OK
api_1     | INFO:     192.168.240.4:51518 - "GET /api/sensors/None/occupancy HTTP/1.1" 404 Not Found
```

**Running tests**


```shell
$ docker-compose down && docker-compose up --build -d && docker-compose exec api python -m pytest

====================================================================================================== test session starts =======================================================================================================
platform linux -- Python 3.10.1, pytest-7.1.1, pluggy-1.0.0
rootdir: /usr/src/app, configfile: pytest.ini
plugins: anyio-3.5.0
collected 9 items                                                                                                                                                                                                                

tests/functional/functional_scenario_test.py::test_scenario PASSED                                                                                                                                                         [ 11%]
tests/unit/api_is_up_test.py::test_home_page PASSED                                                                                                                                                                        [ 22%]
tests/unit/get_sensors_list_test.py::test_get_sensor_list PASSED                                                                                                                                                           [ 33%]
tests/unit/occupancy_at_instant_nok_test.py::test_occupancy_at_instant_sensors_empty PASSED                                                                                                                                [ 44%]
tests/unit/occupancy_at_instant_ok_test.py::test_occupancy_at_instant PASSED                                                                                                                                               [ 55%]
tests/unit/occupancy_nok_test.py::test_occupancy_nok PASSED                                                                                                                                                                [ 66%]
tests/unit/occupancy_ok_test.py::test_occupancy PASSED                                                                                                                                                                     [ 77%]
tests/unit/webhook_query_nok_test.py::test_webhook_query_nok PASSED                                                                                                                                                        [ 88%]
tests/unit/webhook_query_ok_test.py::test_webhook_query_ok PASSED                                                                                                                                                          [100%]

======================================================================================================= 9 passed in 0.32s ========================================================================================================
```

### API documentation -- OpenAPI

API documentation is available, after booting the stack through :
>$docker-compose down && docker-compose up --build -d 

Lien pour la documentation : 
>http://127.0.0.1/docs


__Swagger Documentation__

<img src="resources/images/api.png" alt="Welcome page" title="Frontend Screenshot" width="90%" height="60%">