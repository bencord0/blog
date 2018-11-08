import graphene

from graphene_django.types import DjangoObjectType
from blog.models import Entry


class EntryType(DjangoObjectType):
    class Meta:
        model = Entry

    summary = graphene.String(required=True)
    html = graphene.String(required=True)
    fuzzy_date = graphene.String(required=True)
    url = graphene.String(required=True)


class EntryQuery(object):
    all_entries = graphene.List(EntryType)

    entry = graphene.Field(
        EntryType,
        slug=graphene.String(),
        title=graphene.String(),
    )

    def resolve_all_entries(self, info, **kwargs):
        return Entry.objects.all()

    def resolve_entry(self, info, **kwargs):
        slug = kwargs.get('slug')
        title = kwargs.get('title')

        if slug is not None:
            return Entry.objects.get(slug=slug)

        if title is not None:
            return Entry.objects.get(title=title)

        return None

class RootQuery(EntryQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=RootQuery)
