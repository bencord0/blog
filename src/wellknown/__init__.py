from django.conf import settings
from django.http import HttpResponse


def keybase(request):
    content = b''
    code = 404

    if settings.WELLKNOWN_KEYBASE:
        try:
            with open(settings.WELLKNOWN_KEYBASE, 'rb') as f:
                content = f.read()
                code = 200
        except FileNotFoundError:
            pass

    return HttpResponse(
        content,
        content_type='text/plain' if content else None,
        status=code)
