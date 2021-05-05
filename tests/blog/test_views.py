# Copyright (C) 2016-2021 Ben Cordero <bencord0@condi.me>
#
# This file is part of blog.condi.me.
#
# blog.condi.me is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# blog.condi.me is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with blog.condi.me.  If not, see <http://www.gnu.org/licenses/>.

import pytest

from blog.models import Entry

from tests.factories.entry import EntryFactory


def test_trailing_slash_redirect(client):
    response = client.get("/withoutslash")
    assert response.status_code == 301
    assert response.get('location') == '/withoutslash/'


@pytest.mark.django_db
def test_404(client):
    response = client.get("/nonexistant/")
    assert response.status_code == 404


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
class TestIndex(object):
    def test_index(self, client):
        response = client.get("/")
        assert response.status_code == 200
        assert "Fragments" in response.content.decode()

    def test_index_with_entry(self, client):
        slug = EntryFactory.create().slug
        assert Entry.objects.exists()

        response = client.get("/")

        assert response.status_code == 200
        assert f'href="/{slug}/"' in response.content.decode()


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
class TestSlug(object):
    def test_slug(self, client):
        entry = EntryFactory.create()

        response = client.get(f"/{entry.slug}/")
        assert response.status_code == 200
        assert entry.slug in response.content.decode()


@pytest.mark.django_db
def test_about(client):
    response = client.get("/about/")
    assert response.status_code == 200
    assert "Ben Cordero" in response.content.decode()


@pytest.mark.django_db
def test_archive(client):
    response = client.get("/archive/")
    assert response.status_code == 200


def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.content == b''
