import datetime
import glob
import json

import arrow

from collections import namedtuple
from markdown import Markdown

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

        entries[entry['date']] = get_entry(entry['slug'])

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
    published = arrow.get(date)
    return published.humanize()
