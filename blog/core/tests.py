import datetime

from django.test import TestCase
from blog.core.utils import *


class TestDateTuple(TestCase):
    def test_datetuple(self):
        utcnow = datetime.datetime.utcnow()
        isonow = utcnow.isoformat()
        isodate = isonow.split('T', 1)[0].split('-')

        tuplenow = datetuple(*map(int, isodate))

        assert tuplenow.year == utcnow.year
        assert tuplenow.month == utcnow.month
        assert tuplenow.day == utcnow.day
