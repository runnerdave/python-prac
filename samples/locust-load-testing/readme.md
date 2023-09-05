# Test of the locust tool

[website](https://locust.io/)

[documentation](https://docs.locust.io/en/stable/installation.html)

## Sample run

    locust -f locustfile.py

Then go to: http://0.0.0.0:8089/

Initially received the following error:

    GET /en/latest/: SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)')

So the documentation recommends to use FastHttpUser to inherit instead of HttpUser: https://docs.locust.io/en/stable/increase-performance.html#fasthttpsession-class

As it uses insecure mode as default
