from django.http import HttpResponse
from django.shortcuts import render

from .forms import SearchForm
from .utils import (
    get_all_entries, get_entry, get_recent_entries, search_entries
)


def default_context():
    return {
        'recent_entries': get_recent_entries(),
        'form': SearchForm(),
    }


def index(request):
    context = default_context()
    response = render(request, 'index.html.j2', context)
    return response


def slug(request, slug):
    entry = get_entry(slug)
    context = default_context() | {
        'entry': entry,
        'html': entry.html,
    }
    response = render(request, 'entry.html.j2', context)
    return response


def about(request):
    context = default_context()
    return render(request, 'about.html.j2', context)


def archive(request):
    all_entries = get_all_entries()
    context = default_context() | {
        'all_entries': all_entries,
    }
    return render(request, 'archive.html.j2', context)


def search(request):
    query = request.GET.get('q', '')
    entries = search_entries(query)

    context = default_context() | {
        'query': query,
        'entries': entries,
    }
    return render(request, 'search.html.j2', context)


def health(request):
    return HttpResponse('')
