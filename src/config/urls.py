from django.conf.urls import handler404, url
from django.utils.functional import curry
from django.views.defaults import page_not_found

import wellknown

import blog.api
import blog.feeds
import blog.views


urlpatterns = [
    url(r'^$', blog.views.index, name='index'),
    url(r'^about/$', blog.views.about, name='about'),
    url(r'^archive/$', blog.views.archive, name='archive'),
    url(r'^feeds/atom/$', blog.feeds.atom, name='atom'),
    url(r'^feeds/rss/$', blog.feeds.rss, name='rss'),
    url(r'^api/md/(?P<slug>[a-z0-9-_]+)/$', blog.api.md, name='md-slug'),
    url(r'^api/(?P<slug>[a-z0-9-_]+)/(?P<item>[a-z][a-z_]+)/$',
        blog.api.item, name='api-item'),
    url(r'^api/(?P<slug>[a-z0-9-_]+)/$', blog.api.slug, name='api-slug'),
    url(r'^api/$', blog.api.index, name='api-index'),
    url(r'^.well-known/keybase.txt$',
        wellknown.keybase, name='wellknown-keybase'),
    url(r'^(?P<slug>[a-z0-9-_]+)/$', blog.views.slug, name='slug'),
]

handler404 = curry(page_not_found, template_name='404.html.j2')  # noqa: F811