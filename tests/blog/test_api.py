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
