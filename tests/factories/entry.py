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

import string
from datetime import datetime

import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from blog.models import Entry


class EntryFactory(DjangoModelFactory):
    class Meta:
        model = Entry

    slug = fuzzy.FuzzyText('slug-', chars=string.ascii_lowercase)
    title = fuzzy.FuzzyText('title-')
    date = factory.LazyFunction(datetime.now)
