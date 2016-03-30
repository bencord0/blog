import datetime
import glob
import json

from collections import namedtuple
from markdown import Markdown

datetuple = namedtuple('datetuple', ['year', 'month', 'day'])
_md = Markdown().convert


def _add_summary(entry):
    with open('markdown/{}.md'.format(entry['slug'])) as f:
        markup = f.read()
        summary = _md(markup).split('</p>', 1)[0]
        entry['summary'] = summary
    return entry


def get_recent_entries(count=10):
    entries = {}
    for filename in glob.glob('metadata/*.json'):
        with open(filename) as f:
            entry = json.loads(f.read())

        entries[entry['date']] = entry

    recent_entries = [entries[d] for d in sorted(entries.keys())]
    recent_entries.reverse()

    recent_entries = list(map(_add_summary, recent_entries[:count]))

    return recent_entries



def get_entry(slug):
    with open('metadata/{}.json'.format(slug)) as f:
        entry = json.loads(f.read())

    with open('markdown/{}.md'.format(slug)) as f:
        markup = f.read()
        html = _md(markup)
        summary = html.split('</p>', 1)[0]

    entry['md'] = markup
    entry['html'] = html
    entry['summary'] = summary
    entry['fuzzy_date'] = fuzzy_date(entry['date'])
    return entry


def fuzzy_date(date):
    # tuple(year, month, day)
    published = date.split('T', 1)[0].split('-')
    published = datetuple(*map(int, published))

    current = datetime.datetime.utcnow().date()
    if published.year != current.year:
        delta_y = current.year - published.year
        if delta_y == 1:
            return 'last year'
        return '{} years ago'.format(delta_y)

    if published.month != current.month:
        delta_m = current.month - published.month
        if delta_m == 1:
            return 'last month'
        return '{} months ago'.format(delta_m)

    if published.day != current.day:
        delta_d = current.day - published.day
        if delta_d == 0:
            return 'today'
        if delta_d == 1:
            return 'yesterday'
        if delta_d == 2:
            return 'two days ago'
        if delta_d == 3:
            return 'three days ago'
        if delta_d == 4:
            return 'four days ago'
        if delta_d == 5:
            return 'five days ago'
        if delta_d == 6:
            return 'six days ago'
        if delta_d >= 7 and delta_d < 14:
            return 'last week'
        if delta_d >= 14 and delta_d < 21:
            return 'two weeks ago'
        if delta_d >= 21 and delta_d < 28:
            return 'three weeks ago'
        if delta_d >= 28 and delta_d < 35:
            return 'four weeks ago'

        # A catch all for future dates and timesync issues
        return ''
