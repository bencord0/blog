import mimetypes
import os

from twisted.python.filepath import FilePath
from twisted.web.server import NOT_DONE_YET
from twisted.web.static import NoRangeStaticProducer


class StaticDirectory:
    def __init__(self, staticdir, staticprefix):
        """
        staticdir: On disk path to the directory root of static files
        staticprefix: Prefix to strip from a request URI to get the filename.
        """
        self.dir = staticdir
        self.prefix = staticprefix

    def GET(self, request):
        # TODO: set mimetypes

        request.setHeader('Accept-Ranges', 'Bytes')

        path = request.uri[len(self.prefix):].decode()
        path = os.path.join(self.dir, path)
        path = os.path.abspath(path)

        if not os.path.exists(path):
            request.setResponseCode(404)
            request.finish()
            return NOT_DONE_YET

        # TODO: directory listings
        if os.path.isdir(path):
            request.setResponseCode(403)
            request.finish()
            return NOT_DONE_YET

        try:
            # TODO: handle HTTP HEAD (no response body)
            static_file = FilePath(path)

            # TODO: set and check caching and range headers
            mime, encoding = mimetypes.guess_type(path)
            contenttype = mime or 'application/octet-stream'
            if encoding:
                contenttype += '; charset={}'.format(encoding)
            request.setHeader(
                'Content-Type', contenttype)
            request.setHeader(
                'Content-Length', '{}'.format(static_file.getsize()))

            NoRangeStaticProducer(request, static_file.open()).start()
            return NOT_DONE_YET

        except IOError:
            request.setResponseCode(403)
            request.finish()
            return NOT_DONE_YET
