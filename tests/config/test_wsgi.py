from config.wsgi import application

from django.test import Client

import pytest


@pytest.mark.django_db
class TestApplication:
    def test_wsgi(self, settings):
        settings.ALLOWED_HOSTS = ['']

        # A dud request is quickly rejected as a bad client request.
        client = Client(application)

        response = client.get("/")
        assert response.status_code == 400

    def test_allowed_wsgi(self, settings):
        settings.ALLOWED_HOSTS = ['testserver']

        # A clean request is quickly accepted as a good request.
        client = Client(application)

        response = client.get("/")
        assert response.status_code == 200
