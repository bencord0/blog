import types

from twisted.internet import endpoints
from twisted.internet.defer import Deferred, ensureDeferred
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET, Site


def Http404(request):
    request.setResponseCode(404)
    return b'<h1>404 Not Found</h1>'


def Http405(request):
    request.setResponseCode(405)
    return b'<h1>405 Method not Allowed</h1>'


class WebServer(Resource):
    isLeaf = True

    def __init__(self, reactor, port, urlmap):
        self.urlmap = urlmap
        factory = Site(self)
        endpoint = endpoints.TCP6ServerEndpoint(reactor, port)
        endpoint.listen(factory)

    def render(self, request):
        # TODO: request takes *args

        for path, view in self.urlmap:
            if request.uri == path:
                renderer = getattr(view, request.method.decode(), Http405)
                break
        else:
            renderer = Http404

        d = renderer(request)
        if isinstance(d, types.CoroutineType):
            d = ensureDeferred(d)
        if isinstance(d, Deferred):
            d = NOT_DONE_YET
        return d
