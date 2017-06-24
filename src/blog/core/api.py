from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.core.models import Entry


class EntryResource(APIView):
    def get(self, request, slug):
        entry = get_object_or_404(Entry, slug=slug)
        return Response(entry.as_dict())


def md(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return HttpResponse(
        entry.md, content_type='text/x-markdown; charset=UTF-8')


@api_view(['GET'])
def item(request, slug, item):
    entry = get_object_or_404(Entry, slug=slug)
    try:
        return Response({item: entry.as_dict()[item]})
    except KeyError:
        raise Http404


@api_view(['GET'])
def index(request):
    entries = Entry.objects.order_by('-date').values('slug', 'title', 'date')
    return Response(entries)


slug = EntryResource.as_view()