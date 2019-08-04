from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Entry
from .serializers import SummaryEntrySerializer


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
    entries = Entry.objects.order_by('-date')
    serializer = SummaryEntrySerializer(entries, many=True)
    return Response(
        serializer.data,
        headers={'Access-Control-Allow-Origin': '*'},
    )


slug = EntryResource.as_view()
