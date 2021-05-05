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

from blog.management.commands.import_entries import process_entry
from blog.models import Entry

from tests.factories.entry import EntryFactory


@pytest.mark.django_db
class TestProcessEntry(object):
    def test_invalid_entry(self):
        with pytest.raises(KeyError):
            process_entry({}, '')

    def test_process_entry(self):
        e = EntryFactory.build()

        assert not Entry.objects.exists()
        process_entry({
            'slug': e.slug,
            'title': e.title,
            'date': str(e.date),
        }, '')

        entry = Entry.objects.get()
        assert entry.slug == e.slug
        assert entry.title == e.title

    def test_process_entry_again(self):
        e = EntryFactory.build()

        assert not Entry.objects.exists()

        process_entry({
            'slug': e.slug,
            'title': e.title,
            'date': str(e.date),
        }, '')
        assert Entry.objects.count() == 1

        process_entry({
            'slug': e.slug,
            'title': e.title,
            'date': str(e.date),
        }, '')
        assert Entry.objects.count() == 1

    def test_process_multiple_entries(self):
        e1 = EntryFactory.build()
        e2 = EntryFactory.build()

        assert e1 != e2
        assert not Entry.objects.exists()

        process_entry({
            'slug': e1.slug,
            'title': e1.title,
            'date': str(e1.date),
        }, '')
        assert Entry.objects.count() == 1

        process_entry({
            'slug': e2.slug,
            'title': e2.title,
            'date': str(e2.date),
        }, '')
        assert Entry.objects.count() == 2

        assert Entry.objects.get(slug=e1.slug).slug == e1.slug
        assert Entry.objects.get(slug=e2.slug).slug == e2.slug

    @pytest.mark.parametrize("md,expected,html", [
        ("", "", ""),
        ("foo", "foo", "<p>foo</p>"),
        ("# foo", "# foo", "<h1>foo</h1>"),
    ])
    def test_process_entry_md(self, md, expected, html):
        e = EntryFactory.build()
        assert not Entry.objects.exists()

        process_entry({
            'slug': e.slug,
            'title': e.title,
            'date': str(e.date),
        }, md)

        entry = Entry.objects.get()
        assert entry.md == expected
        assert entry.html == html
