# PlusPeter Back End Tech Test

The goal of the task is to develop a service which exposes the following 3 api methods:

1: `GET /temperatures?start=2018-08-01T00:00:00Z&end=2018-08-07T00:00:00Z`

2: `GET /speeds?start=2018-08-01T00:00:00Z&end=2018-08-04T00:00:00Z`

3: `GET /weather?start=2018-08-01T00:00:00Z&end=2018-08-04T00:00:00Z`

Tests included. Dockerfile included.

You can find the complete task description in `TASK.md`.

### Start Web Service

With the command:

```
docker-compose up
```

### For Development:

First, run:

```
docker-compose build web
```

Then, run:

```
docker-compose up -d
```

And then, run web service in Bash:

```
docker-compose run web bash
```