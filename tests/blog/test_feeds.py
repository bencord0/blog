import pytest

from tests.factories.entry import EntryFactory


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_empty_rss(client):
    response = client.get("/feeds/rss/")
    response.status_code == 200

    assert '<title>Fragments Feed</title>' in response.content.decode()


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_rss(client):
    entry = EntryFactory.create()

    response = client.get("/feeds/rss/")
    response.status_code == 200

    assert f'<item><title>{entry.title}</title><link>http://testserver/{entry.slug}/</link>' in response.content.decode()


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_many_rss(client):
    e1 = EntryFactory.create()
    e2 = EntryFactory.create()

    response = client.get("/feeds/rss/")
    response.status_code == 200

    assert f'<item><title>{e1.title}</title><link>http://testserver/{e1.slug}/</link>' in response.content.decode()
    assert f'<item><title>{e2.title}</title><link>http://testserver/{e2.slug}/</link>' in response.content.decode()


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_atom(client):
    response = client.get("/feeds/atom/")
    response.status_code == 200


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_many_atom(client):
    EntryFactory.create()
    response = client.get("/feeds/atom/")
    response.status_code == 200


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_many_atom(client):
    EntryFactory.create()
    EntryFactory.create(md="foo")
    EntryFactory.create(md="bar")
    response = client.get("/feeds/atom/")
    response.status_code == 200
