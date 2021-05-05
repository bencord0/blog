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

    assert (
        f'<item><title>{entry.title}</title>'
        f'<link>http://testserver/{entry.slug}/</link>'
    ) in response.content.decode()


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_many_rss(client):
    e1 = EntryFactory.create()
    e2 = EntryFactory.create()

    response = client.get("/feeds/rss/")
    response.status_code == 200

    assert (
        f'<item><title>{e1.title}</title>'
        f'<link>http://testserver/{e1.slug}/</link>'
    ) in response.content.decode()
    assert (
        f'<item><title>{e2.title}</title>'
        f'<link>http://testserver/{e2.slug}/</link>'
    ) in response.content.decode()


@pytest.mark.django_db
@pytest.mark.usefixtures("dj_cache")
def test_atom(client):
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
