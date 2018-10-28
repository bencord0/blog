import factory
import string

from blog.models import Entry
from datetime import datetime
from factory import fuzzy


class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry

    slug = fuzzy.FuzzyText('slug-', chars=string.ascii_lowercase)
    title = fuzzy.FuzzyText('title-')
    date = factory.LazyFunction(datetime.now)
