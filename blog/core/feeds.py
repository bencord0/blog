from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed


class RssBlogFeed(Feed):
    pass


class AtomBlogFeed(RssBlogFeed):
    feed_type = Atom1Feed


atom = AtomBlogFeed()
rss = RssBlogFeed()
