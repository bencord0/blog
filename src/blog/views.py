from django.http import HttpResponse
from django.shortcuts import render

from .forms import SearchForm
from .utils import get_all_entries, get_entry, get_recent_entries, search_entries


def index(request):
    recent_entries = get_recent_entries()
    context = {
        'recent_entries': recent_entries,
    }
    response = render(request, 'index.html.j2', context)
    return response


def slug(request, slug):
    entry = get_entry(slug)
    recent_entries = get_recent_entries()
    context = {
        'entry': entry,
        'html': entry.html,
        'recent_entries': recent_entries,
    }
    response = render(request, 'entry.html.j2', context)
    return response


def about(request):
    recent_entries = get_recent_entries()
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


def search(request):
    query = request.GET.get('q', '')
    entries = search_entries(query)
    form = SearchForm()

    context = {
        'query': query,
        'entries': entries,
        'form': form,
    }
    return render(request, 'search.html.j2', context)


def health(request):
    return HttpResponse('')
