from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_recent_entries, get_entry


def index(request):
    recent_entries = get_recent_entries(10)
    return render(request, 'index.html.j2', {
        'recent_entries': recent_entries,
    })


def slug(request, slug):
    entry = get_entry(slug)
    recent_entries = get_recent_entries(10)
    return render(request, 'entry.html.j2', {
        'entry': entry,
        'html': entry['html'],
        'recent_entries': recent_entries,
    })
