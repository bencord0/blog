import string
from datetime import datetime

import factory
from factory import fuzzy

from blog.models import Entry


class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry

    slug = fuzzy.FuzzyText('slug-', chars=string.ascii_lowercase)
    title = fuzzy.FuzzyText('title-')
    date = factory.LazyFunction(datetime.now)
