import io

import pytest


@pytest.mark.django_db
def test_application():
    from config.wsgi import application
    from werkzeug.test import Client

    # A dud request is quickly rejected as a bad client request.
    client = Client(application)

    _, status, _= client.get("/")
    assert status == '400 Bad Request'
