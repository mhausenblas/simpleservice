# A Simple Service

A simple and configurable service that can, for example, be used for testing container orchestration setups (incl. health check endpoint).

Note that the versions of `simpleservice`, such as `0.4.0`, used in the following refer to the tags used in the respective [Docker images](https://hub.docker.com/r/mhausenblas/simpleservice/tags/) created. There are no tags or releases as such in this GitHub repo.

Contents:

- [The HTTP API](#the-http-api)
- [Running it](#running-it)
- [Changing runtime behaviour](#changing-runtime-behaviour)
- [Invoking it](#invoking-it)

## The HTTP API

In addition to the endpoints listed here, see also the [change the runtime behaviour](#changing-runtime-behaviour) section below. 

### `/env` [0.5.0+]

Principled response:

    HTTP/1.1 200 OK
    $HEADER_FIELDS
     {
         "env": "$DUMP_OF_ENVIRONMENT_VARS",
         "version": "$VERSION"
     }

Example response:

    HTTP/1.1 200 OK                                                                                                                                                             [5/99]
    Content-Length: 2471
    Content-Type: application/json
    Date: Mon, 24 Apr 2017 12:38:47 GMT
    Etag: "5ccb76cf1545f01fd1e0df4257ff6f8da19678e9"
    Server: TornadoServer/4.3

    {
        "env": "{'USER': 'mhausenblas', ...}"
        "version": "0.5.0"
    }    

### `/info` [0.5.0+]

Principled response:

    HTTP/1.1 200 OK
    $HEADER_FIELDS
     {
         "from": "$REMOTE_IP",
         "host": ""$HOST:$PORT"",
         "version": "$VERSION"
     }

Example response:

    HTTP/1.1 200 OK
    Content-Length: 67
    Content-Type: application/json
    Date: Mon, 24 Apr 2017 12:36:37 GMT
    Etag: "9d09b0a126f68a0fddfec0f494e56fcab29eac15"
    Server: TornadoServer/4.3

    {
        "from": "127.0.0.1",
        "host": "localhost:9876",
        "version": "0.5.0"
    }


### `/health` [0.4.0+]

Principled response:

    HTTP/1.1 200 OK
    $HEADER_FIELDS
     {
         "healthy": true
     }

Example response:

    HTTP/1.1 200 OK
    Content-Length: 17
    Content-Type: application/json
    Date: Tue, 11 Oct 2016 17:17:21 GMT
    Etag: "b40026a9bea9f5096f4ef55d3d23d6730139ff5e"
    Server: TornadoServer/4.3

    {
        "healthy": true
    }

### `/endpoint0` [0.3.0+]

Principled response:

    HTTP/1.1 200 OK
    $HEADER_FIELDS
    {
        "host": "$HOST:$PORT",
        "result": "all is well",
        "version": "$VERSION"
    }

Example response:

    HTTP/1.1 200 OK
    Content-Length: 71
    Content-Type: application/json
    Date: Tue, 11 Oct 2016 16:57:33 GMT
    Etag: "ce18606c019e1d8c584b796d1fe7402d9767b9b6"
    Server: TornadoServer/4.3

    {
        "host": "localhost:9876",
        "result": "all is well",
        "version": "0.4.0"
    }

## Running it

For local execution, Python `2.7.9` is required. You can then run `simpleservice` like so:

    # with defaults:
    $ python simpleservice.py

    # overwriting certain runtime settings:
    $ HEALTH_MAX=200 VERSION=1.0 python simpleservice.py

If you fancy it you can run the containerized version of `simpleservice` on your local machine (requires Docker installed):

    $ docker run -P mhausenblas/simpleservice:0.5.0

See also the [container images](https://hub.docker.com/r/mhausenblas/simpleservice/tags/).


## Changing runtime behaviour

Through setting the following environment variables, you can change the runtime behaviour of `simpleservice`:

- `PORT0` ... the port `simpleservice` is serving on
- `VERSION` ... the value of `version` returned in the JSON response of the `/endpoint0` endpoint
- `HEALTH_MIN` and `HEALTH_MAX` ... the min. and max. delay in milliseconds that the `/health` endpoint responds

## Invoking it

Once `simpleservice` is started you can invoke it like so (here is a local service execution shown):

    $ http localhost:9876/endpoint0
    HTTP/1.1 200 OK
    Content-Length: 71
    Content-Type: application/json
    Date: Tue, 11 Oct 2016 16:57:33 GMT
    Etag: "ce18606c019e1d8c584b796d1fe7402d9767b9b6"
    Server: TornadoServer/4.3

    {
        "host": "localhost:9876",
        "result": "all is well",
        "version": "0.4.0"
    }

And the service logs would show something like:

    ~$ python simpleservice.py
    This is a simple service in version v0.4.0 listening on port 9876
    2016-10-11T05:57:33 INFO /endpoint0 serving from localhost:9876 has been invoked from 127.0.0.1 [at line 58]
    2016-10-11T05:57:33 INFO 200 GET /endpoint0 (127.0.0.1) 1.10ms [at line 1946]

Note that the available endpoints depend on the version of `simpleservice` as defined in the first section of this docs (aka API).
