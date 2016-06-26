from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_recent_entries, get_entry


def index(request):
    recent_entries = get_recent_entries(10)
    context = {
        'recent_entries': recent_entries,
    }
    return render(request, 'index.html.j2', context)


def slug(request, slug):
    entry = get_entry(slug)
    recent_entries = get_recent_entries(10)
    context = {
        'entry': entry,
        'recent_entries': recent_entries,
    }
    return render(request, 'entry.html.j2', context)


def about(request):
    recent_entries = get_recent_entries(10)
    context = {
        'recent_entries': recent_entries,
    }
    return render(request, 'about.html.j2', context)
