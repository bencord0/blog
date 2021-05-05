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

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Entry


class EntryResource(APIView):
    def get(self, request, slug):
        entry = get_object_or_404(Entry, slug=slug)
        return Response(
            entry.as_dict(),
            headers={'Access-Control-Allow-Origin': '*'},
        )


def md(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    response = HttpResponse(
        entry.md,
        content_type='text/x-markdown; charset=UTF-8',
    )
    response.setdefault('Access-Control-Allow-Origin', '*')
    return response


@api_view(['GET'])
def item(request, slug, item):
    entry = get_object_or_404(Entry, slug=slug)
    try:
        return Response(
            {item: entry.as_dict()[item]},
            headers={'Access-Control-Allow-Origin': '*'},
        )
    except KeyError:
        raise Http404


@api_view(['GET'])
def index(request):
    entries = Entry.objects.order_by('-date').values('slug', 'title', 'date')
    return Response(
        entries,
        headers={'Access-Control-Allow-Origin': '*'},
    )


slug = EntryResource.as_view()
