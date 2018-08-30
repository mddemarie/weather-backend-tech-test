# PlusPeter Back End Tech Test

The goal of the task is to develop a service which exposes the following 1 api method:

`GET /temperatures?start=2018-08-01T00:00:00Z&end=2018-08-07T00:00:00Z`

Tests included. Dockerfile & Docker-compose setup included.

You can find the complete task description in `TASK.md`.

### Start Web Service

With the command:

```
docker-compose up
```

### In Browser

Go to the url:

```
http://localhost:8001/temperatures?start=2018-08-01T00:00:00Z&end=2018-08-07T00:00:00Z
```

I use the port 8001.


### Integration Tests

Run the test with the command:

```
python3 manage.py test
```

### Unit Tests

Run the tests with the commands:

```
python3 -m unittest temperature/test_data.py
python3 -m unittest temperature/test_client.py
```

#### Non-working:
- curl command and the whole url above
- the integration test shows that the GET method returns html and 404

#### Working:

- the algorithm for getting the temperatures from external service - the algorithm returns the data in an expected JSON format
- unit tests pass
- Docker & Docker-compose setup is correct