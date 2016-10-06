import os

from blog import settings
from blog.core import WebServer

from twisted.internet import reactor


def main():
    PORT = os.getenv('PORT', 8000)
    WebServer(reactor, settings.PORT, settings.URLMAP)

    print("Started server on port {}".format(PORT))
    reactor.run()

if __name__ == '__main__':
    main()
