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
