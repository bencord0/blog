from django.shortcuts import render

from .utils import get_all_entries, get_entry, get_recent_entries


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


def archive(request):
    all_entries = get_all_entries()
    recent_entries = all_entries[:10]
    context = {
        'recent_entries': recent_entries,
        'all_entries': all_entries,
    }
    return render(request, 'archive.html.j2', context)
