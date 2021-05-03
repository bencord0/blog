from django.db import connections

import pytest

from tests.factories.entry import EntryFactory

db_engine = connections.databases['default']['ENGINE']
need_postgres = pytest.mark.skipif(
    db_engine != 'django.db.backends.postgresql_psycopg2',
    reason='need postgres for search feature')


@pytest.mark.django_db
@need_postgres
class TestSearch:

    def test_search(self, client):
        response = client.get("/search/")
        assert response.status_code == 200

    def test_search_query(self, client):
        EntryFactory.create(md="""
            An entry about python.
        """)

        response = client.get("/search/?q=python")
        assert response.status_code == 200
        assert "An entry about python" in response.content.decode()
