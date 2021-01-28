import pytest

from blog.models import Entry

from tests.factories.entry import EntryFactory


@pytest.mark.django_db
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
