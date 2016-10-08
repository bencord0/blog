import types

from twisted.internet import endpoints
from twisted.internet.defer import Deferred, ensureDeferred
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET, Site
from blog.static import StaticDirectory


async def Response(request, body='', headers=None, code=200):
    if headers is None:
        headers = {}

    request.setResponseCode(code)
    for header, value in headers.items():
        request.setHeader(header, value)

    request.write(body.encode())
    request.finish()


async def redirect(request, url):
    request.redirect(url)
    request.finish()


def Http404(request):
    request.setResponseCode(404)
    return b'<h1>404 Not Found</h1>'


def Http405(request):
    request.setResponseCode(405)
    return b'<h1>405 Method not Allowed</h1>'


class WebServer(Resource):
    isLeaf = True

    def __init__(self, reactor, port, urlmap, *,
                 staticdir=None, staticprefix=None,
                 Http404=Http404, Http405=Http405):
        self.urlmap = urlmap
        factory = Site(self)
        endpoint = endpoints.TCP6ServerEndpoint(reactor, port)
        endpoint.listen(factory)

        self.staticprefix = staticprefix
        if staticprefix and staticdir:
            self.static = StaticDirectory(staticdir, staticprefix)


        self.Http404 = Http404
        self.Http405 = Http405

    def render(self, request):
        # TODO: request takes *args

        for path, view in self.urlmap:
            if self.staticprefix and request.uri.startswith(self.staticprefix):
                renderer = getattr(self.static,
                                   request.method.decode(),
                                   self.Http405)
                break
            if request.uri == path:
                renderer = getattr(view,
                                   request.method.decode(),
                                   self.Http405)
                break
        else:
            renderer = self.Http404

        d = renderer(request)
        if isinstance(d, types.CoroutineType):
            d = ensureDeferred(d)
        if isinstance(d, Deferred):
            d = NOT_DONE_YET

        return d
