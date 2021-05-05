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

from config.wsgi import application

from django.test import Client

import pytest


@pytest.mark.django_db
class TestApplication:
    def test_wsgi(self, settings):
        settings.ALLOWED_HOSTS = ['']

        # A dud request is quickly rejected as a bad client request.
        client = Client(application)

        response = client.get("/")
        assert response.status_code == 400

    def test_allowed_wsgi(self, settings):
        settings.ALLOWED_HOSTS = ['testserver']

        # A clean request is quickly accepted as a good request.
        client = Client(application)

        response = client.get("/")
        assert response.status_code == 200
