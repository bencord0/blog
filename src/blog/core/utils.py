import datetime
from dateutil.parser import parse as _parse_date

from blog.core.models import Entry


def get_all_entries():
    return Entry.objects.order_by('-date')


def get_recent_entries(count=10):
    return Entry.objects.order_by('-date')[:count]


def get_entry(slug):
    return Entry.objects.get(slug=slug)


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
