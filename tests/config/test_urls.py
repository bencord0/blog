from django.test import Client

import pytest

client = Client()


@pytest.mark.django_db
def test_nonexistant_page():
    response = client.get('/nonexistant/')
    assert response.status_code == 404
