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
