from twisted.internet import endpoints, reactor
from twisted.web.server import Site

from blog import app, settings


def main():
    ep = endpoints.serverFromString(reactor, settings.SERVER_DESCRIPTION)
    s = Site(app.resource())
    ep.listen(s)
    print("Listening on " + settings.SERVER_DESCRIPTION)
    reactor.run()


if __name__ == "__main__":
    main()
