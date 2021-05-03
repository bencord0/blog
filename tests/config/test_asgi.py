from asgi_testclient import TestClient as Client

from config.asgi import application

import pytest


@pytest.mark.asyncio
@pytest.mark.django_db
class TestApplication:
    async def test_asgi(self, settings):
        settings.ALLOWED_HOSTS = ['']

        # A dud request is quickly rejected as a bad client request.
        client = Client(application)

        response = await client.get("/")
        assert response.status_code == 400

    async def test_allowed_asgi(self, settings):
        settings.ALLOWED_HOSTS = ['testserver']

        # A clean request is quickly accepted as a good request.
        client = Client(application)

        response = await client.get("/")
        assert response.status_code == 200
