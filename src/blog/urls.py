from django.conf.urls import url
# from django.contrib import admin

import blog.core.api
import blog.core.feeds
import blog.core.views

urlpatterns = [
#     url(r'^admin/', admin.site.urls),
    url(r'^$', blog.core.views.index, name='index'),
    url(r'^about/$', blog.core.views.about, name='about'),
    url(r'^archive/$', blog.core.views.archive, name='archive'),
    url(r'^feeds/atom/$', blog.core.feeds.atom, name='atom'),
    url(r'^feeds/rss/$', blog.core.feeds.rss, name='rss'),
    url(r'^api/md/(?P<slug>[a-z0-9-_]+)/$', blog.core.api.md, name='md-slug'),
    url(r'^api/(?P<slug>[a-z0-9-_]+)/(?P<item>[a-z][a-z_]+)/$', blog.core.api.item, name='api-item'),
    url(r'^api/(?P<slug>[a-z0-9-_]+)/$', blog.core.api.slug, name='api-slug'),
    url(r'^(?P<slug>[a-z0-9-_]+)/$', blog.core.views.slug, name='slug'),
]
