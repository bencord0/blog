import pytest

from tests.factories.entry import EntryFactory


def _coerce_date(d):
    return str(d).replace("+00:00", "Z").replace(" ", "T")


def _coerce_date_on_entry(e):
    e['date'] = _coerce_date(e['date'])
    return e


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
class TestIndex(object):
    def test_without_entries(self, client):
        response = client.get("/api/")

        assert response.status_code == 200
        assert response.json() == []

    def test_with_entry(self, client):
        entry = EntryFactory.create()

        response = client.get("/api/")

        assert response.status_code == 200
        assert response.json() == [{
            "slug": entry.slug,
            "title": entry.title,
            "date": _coerce_date(entry.date),
        }]


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
class TestEntry(object):
    def test_redirected_entry(self, client):
        response = client.get("/api/redirect")

        assert response.status_code == 301
        assert response.get("location") == "/api/redirect/"

    def test_nonexistant_entry(self, client):
        response = client.get("/api/nonexistant/")

        assert response.status_code == 404

    def test_entry(self, client):
        entry = EntryFactory.create()
        response = client.get(f"/api/{entry.slug}/")

        assert response.status_code == 200
        assert response.json() == _coerce_date_on_entry(entry.as_dict())

    def test_md(self, client):
        entry = EntryFactory.create(md="foo")
        response = client.get(f"/api/md/{entry.slug}/")

        assert response.status_code == 200
        assert response.content.decode() == "foo"

    def test_item(self, client):
        entry = EntryFactory.create(md="foo")
        response = client.get(f"/api/{entry.slug}/html/")

        assert response.status_code == 200
        assert response.json() == {
            "html": "<p>foo</p>"
        }

    def test_nonexistant_item(self, client):
        entry = EntryFactory.create()
        response = client.get(f"/api/{entry.slug}/nonexistant/")

        assert response.status_code == 404
