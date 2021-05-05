# Copyright (C) 2016-2021 Ben Cordero <bencord0@condi.me>
#
# This file is part of blog.condi.me.
#
# blog.condi.me is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# blog.condi.me is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with blog.condi.me.  If not, see <http://www.gnu.org/licenses/>.

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
