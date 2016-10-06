import blog.core

from twisted.internet import reactor


def test_blog():
    blog.core.WebServer(reactor, 1, tuple())
