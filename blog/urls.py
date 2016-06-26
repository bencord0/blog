from django.conf.urls import url
# from django.contrib import admin

import blog.core.views
import blog.core.feeds

urlpatterns = [
#     url(r'^admin/', admin.site.urls),
    url(r'^$', blog.core.views.index),
    url(r'^about/$', blog.core.views.about),
    url(r'^(?P<slug>[a-z0-9-]+)/$', blog.core.views.slug),
    url(r'^feeds/atom/$', blog.core.feeds.atom),
    url(r'^feeds/rss/$', blog.core.feeds.rss),
]
