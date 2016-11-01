from django.conf import settings
from django.http import HttpResponse


def keybase(request):
    if settings.WELLKNOWN_KEYBASE:
        with open(settings.WELLKNOWN_KEYBASE, 'rb') as f:
            content = f.read()
            code = 200
    else:
        content = b''
        code = 404

    return HttpResponse(content,
                        content_type='text/plain' if content else None,
                        status=code)
