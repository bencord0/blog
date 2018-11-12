import graphene

from graphene_django.types import DjangoObjectType
from blog.models import Entry
from blog.utils import get_entry, get_recent_entries

class EntryType(DjangoObjectType):
    class Meta:
        model = Entry

    summary = graphene.String(required=True)
    html = graphene.String(required=True)
    fuzzy_date = graphene.String(required=True)
    url = graphene.String(required=True)


class EntryQuery(object):
    recent_entries = graphene.Field(
        graphene.List(EntryType),
        count=graphene.Int(),
    )

    entry = graphene.Field(
        EntryType,
        slug=graphene.String(required=True),
    )

    def resolve_recent_entries(self, info, **kwargs):
        count = kwargs.get('count', 20)
        return list(get_recent_entries(count))

    def resolve_entry(self, info, **kwargs):
        slug = kwargs['slug']
        return get_entry(slug)


class Query(EntryQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
