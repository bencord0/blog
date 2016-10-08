import os

from twisted.internet import reactor

from blog import settings
from blog.core import WebServer
from blog.views import Http404


def main():
    PORT = os.getenv('PORT', 8000)
    WebServer(reactor, settings.PORT, settings.URLMAP,
              staticdir='static', staticprefix=b'/static/',
              Http404=Http404)

    print("Started server on port {}".format(PORT))
    reactor.run()

if __name__ == '__main__':
    main()
