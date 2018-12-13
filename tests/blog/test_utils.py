import datetime
import pytest

from blog.utils import (
    get_all_entries,
    get_recent_entries,
    get_entry,
    parse_date,
    UTC,
)
from django.http.response import Http404
from functools import partial
from tests.factories.entry import EntryFactory

# datetime helper, create datetime objects in the UTC timezone
_dt = partial(datetime.datetime, tzinfo=UTC())


@pytest.mark.django_db
class TestGetAllEntries(object):
    def test_get_all_entries_empty(self):
        entries = get_all_entries()
        assert len(entries) == 0

    def test_get_all_entries_one(self):
        entry = EntryFactory.create()

        entries = get_all_entries()

        assert entry in entries

    def test_get_multiple_entries(self):
        e1 = EntryFactory.create()
        e2 = EntryFactory.create()

        entries = get_all_entries()

        assert set(entries) == {e1, e2}

    def test_get_entries_in_order(self):
        e1 = EntryFactory.create()
        e2 = EntryFactory.create()

        entries = get_all_entries()

        # Retrieved entries are in reverse order by date
        assert list(entries) == [e2, e1]
        assert e1.date < e2.date

    def test_get_lots_of_entries(self):
        ENTRY_COUNT = 100
        ee = [
            EntryFactory.create()
            for _ in range(ENTRY_COUNT)
        ]
        entries = get_all_entries()

        assert set(entries) == set(ee)
        assert entries.count() == ENTRY_COUNT


@pytest.mark.django_db
class TestGetRecentEntries(object):
    def test_get_recent_entries_empty(self):
        entries = get_recent_entries()
        assert len(entries) == 0

    def test_get_recent_entries_one(self):
        entry = EntryFactory.create()

        entries = get_recent_entries()

        assert entry in entries

    def test_get_multiple_entries(self):
        e1 = EntryFactory.create()
        e2 = EntryFactory.create()

        entries = get_recent_entries()

        assert set(entries) == {e1, e2}

    def test_get_entries_in_order(self):
        e1 = EntryFactory.create()
        e2 = EntryFactory.create()

        entries = get_recent_entries()

        # Retrieved entries are in reverse order by date
        assert list(entries) == [e2, e1]
        assert e1.date < e2.date

    def test_get_lots_of_entries(self):
        DEFAULT_ENTRY_COUNT = 20
        ENTRY_COUNT = 100

        ee = {
            EntryFactory.create()
            for _ in range(ENTRY_COUNT)
        }

        entries = get_recent_entries()

        assert all(e in ee for e in entries)
        assert entries.count() != ENTRY_COUNT
        assert entries.count() == DEFAULT_ENTRY_COUNT

    @pytest.mark.parametrize("retrieval_count", [
        0,
        1,
        10,
        20,
        30,
        100,
    ])
    def test_get_specified_number_of_entries(self, retrieval_count):
        ENTRY_COUNT = 100

        ee = {
            EntryFactory.create()
            for _ in range(ENTRY_COUNT)
        }

        entries = get_recent_entries(retrieval_count)

        assert all(e in ee for e in entries)
        assert entries.count() == retrieval_count

    @pytest.mark.parametrize("retrieval_count", [
        10,
        11,
        20,
        30,
        100,
    ])
    def test_get_too_many_entries(self, retrieval_count):
        ENTRY_COUNT = 10

        ee = {
            EntryFactory.create()
            for _ in range(ENTRY_COUNT)
        }

        entries = get_recent_entries(retrieval_count)

        assert all(e in ee for e in entries)
        assert entries.count() == ENTRY_COUNT


@pytest.mark.django_db
class TestGetEntry(object):
    def test_get_nonexistant_entry(self):
        with pytest.raises(Http404):
            get_entry("nonexistant")

    def test_get_entry(self):
        slug = EntryFactory.create().slug

        entry = get_entry(slug)

        assert entry.slug == slug


@pytest.mark.parametrize("date,expected", [
    ('2017-12-17T11:47:33Z', _dt(2017, 12, 17, 11, 47, 33)),
    ('2017-06-25T14:31:24Z', _dt(2017, 6, 25, 14, 31, 24)),
    ('2017-06-21T22:19:18Z', _dt(2017, 6, 21, 22, 19, 18)),
    ('2017-01-23T20:48:17Z', _dt(2017, 1, 23, 20, 48, 17)),
    ('2016-12-24T19:51:20Z', _dt(2016, 12, 24, 19, 51, 20)),
    ('2015-10-12T11:28:23Z', _dt(2015, 10, 12, 11, 28, 23)),
    ('2015-06-28T21:16:57Z', _dt(2015, 6, 28, 21, 16, 57)),
    ('2015-05-01T23:06:46Z', _dt(2015, 5, 1, 23, 6, 46)),
    ('2015-03-17T01:10:08Z', _dt(2015, 3, 17, 1, 10, 8)),
    ('2013-03-09T12:52:18Z', _dt(2013, 3, 9, 12, 52, 18)),
])
def test_parse_date(date, expected):
    parsed_date = parse_date(date)
    assert parsed_date == expected


@pytest.mark.parametrize("date", [
    '',
    'today',
    'yesterday',
    'foo',
    '2000-00-00T00:00:00Z',
    '2000-00-01T00:00:00Z',
    '2000-01-00T00:00:00Z',
    '2000-01-01T25:00:00Z',
    '2000-01-01T00:61:00Z',
    '2000-01-01T00:00:61Z',
    '2000-01-32T00:00:00Z',
    '2000-13-01T00:00:00Z',
])
def test_parse_invalid_date(date):
    with pytest.raises(ValueError):
        parse_date(date)
