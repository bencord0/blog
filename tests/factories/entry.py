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
