import glob
import json
from markdown import Markdown

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    entries = {}
    for filename in glob.glob('metadata/*.json'):
        with open(filename) as f:
            entry = json.loads(f.read())

        entries[entry['date']] = entry

    recent_entries = [entries[d] for d in sorted(entries.keys())]
    recent_entries.reverse()

    return render(request, 'index.html.j2', {
        'recent_entries': recent_entries,
    })


def slug(request, slug):
    with open('metadata/{}.json'.format(slug)) as f:
        metadata = json.loads(f.read())

    with open('markdown/{}.md'.format(slug)) as f:
        markup = _md(f.read())

    return render(request, 'entry.html.j2', {
        'entry': metadata,
        'html': markup,
    })

_md = Markdown().convert
