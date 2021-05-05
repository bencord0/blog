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

import json
from glob import glob
from os.path import abspath, join

from django.core.management.base import BaseCommand

from blog.models import Entry
from blog.utils import parse_date


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', help='Directory to import entries from')

    def handle(self, *args, **kwargs):
        path = kwargs.get('path', '.')
        path = abspath(path)

        print(path)
        for entry_path in glob(join(path, 'metadata/*.json')):
            with open(entry_path) as f:
                entry = json.loads(f.read())
            with open(join(path, f'markdown/{entry["slug"]}.md'), 'rb') as f:
                md = f.read().decode('utf-8')

            process_entry(entry, md)


def process_entry(data, md):
    print(data['slug'])
    entry, _ = Entry.objects.get_or_create(slug=data['slug'])
    entry.date = parse_date(data['date'])
    entry.title = data['title']
    entry.md = md
    entry.save()
