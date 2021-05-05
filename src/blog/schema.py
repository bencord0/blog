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

import graphene
from graphene import relay

from graphene_django.types import DjangoObjectType

from blog import models
from blog.utils import get_entry, get_recent_entries


class Entry(DjangoObjectType):
    class Meta:
        model = models.Entry
        interfaces = (relay.Node,)

    summary = graphene.String(required=True)
    html = graphene.String(required=True)
    fuzzy_date = graphene.String(required=True)
    url = graphene.String(required=True)

    @classmethod
    def get_node(cls, info, slug):
        return get_entry(slug)


class EntryList(relay.Connection):
    class Meta:
        node = Entry


class EntryQuery(object):
    recent_entries = relay.ConnectionField(
        EntryList,
        count=graphene.Int(),
    )

    entry = graphene.Field(
        Entry,
        slug=graphene.String(required=True),
    )

    node = relay.Node.Field(Entry)

    def resolve_recent_entries(self, info, count=20, **kwargs):
        return list(get_recent_entries(count))

    def resolve_entry(self, info, slug=None, **kwargs):
        return get_entry(slug)


class Query(EntryQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
