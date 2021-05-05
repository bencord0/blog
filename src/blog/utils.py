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

import datetime

from dateutil.parser import parse as _parse_date

from django.shortcuts import get_object_or_404

from .models import Entry


def get_all_entries():
    return Entry.objects.order_by('-date')


def get_recent_entries(count=20):
    return Entry.objects.order_by('-date')[:count]


def get_entry(slug):
    return get_object_or_404(Entry, slug=slug)


def search_entries(query):
    return Entry.objects.filter(md__search=query).order_by('-date')


class UTC(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(0)

    dst = utcoffset

    def tzname(self, dt):
        return 'UTC'


def parse_date(date):
    dt = _parse_date(date)
    dt = dt.replace(tzinfo=UTC())
    return dt
