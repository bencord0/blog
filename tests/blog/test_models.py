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


@pytest.mark.django_db
class TestEntry(object):
    def test_entry(self):
        assert not Entry.objects.exists()

        e = Entry.objects.create(
            slug="the-slug",
            title="My Title",
            md="""
this is some text

more text goes in this paragraph
""")

        assert e.html == (
            "<p>this is some text</p>\n"
            "<p>more text goes in this paragraph</p>"
        )
        assert e.summary == "<p>this is some text"
        assert e.fuzzy_date == "just now"
        assert e.get_absolute_url() == "/the-slug/"
