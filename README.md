# A Simple Service

For a direct execution, Python `2.7.9` is expected. You can run the `simpleservice` like so:

    $ python simpleservice.py

Or the containerized version:

    $ docker run -P mhausenblas/simpleservice

Once started you can invoke it like so:

    $ http localhost:9876/endpoint0
    HTTP/1.1 200 OK
    Content-Length: 71
    Content-Type: application/json
    Date: Fri, 23 Sep 2016 12:41:49 GMT
    Etag: "11374af167832fe8646cc1f044b2d0cc2b6f411b"
    Server: TornadoServer/4.3

    {
        "host": "localhost:9876",
        "result": "all is well",
        "version": "0.0.0"
    }