import os

from blog import settings
from blog.core import WebServer
from blog.views import Http404

from twisted.internet import reactor


def main():
    PORT = os.getenv('PORT', 8000)
    WebServer(reactor, settings.PORT, settings.URLMAP,
              staticdir='static', staticprefix=b'/static/',
              Http404=Http404)

    print("Started server on port {}".format(PORT))
    reactor.run()

if __name__ == '__main__':
    main()
