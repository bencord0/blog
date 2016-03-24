import glob
import json
import markdown

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    entries = {}
    for filename in glob.glob('metadata/*.json'):
        with open(filename) as f:
            entry = json.loads(f.read())

        entries[entry['date']] = entry

    recent_entries = sorted(entries.keys())
    recent_entries.reverse()

    html = ''
    for datestamp in recent_entries:
        html += '<p><a href="/{slug}/">{title}</a>&nbsp;{date}</p>\n'.format(
            **entries[datestamp])

    return HttpResponse(html)


def slug(request, slug):
    with open('metadata/{}.json'.format(slug)) as f:
        metadata = json.loads(f.read())

    with open('markdown/{}.md'.format(slug)) as f:
        markup = f.read()

    return HttpResponse(
        '<pre>{}</pre>\n{}'
        .format(json.dumps(metadata), markdown.markdown(markup))
    )
