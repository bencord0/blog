from twisted.internet import reactor

import blog.core


def test_blog():
    blog.core.WebServer(reactor, 1, tuple())
