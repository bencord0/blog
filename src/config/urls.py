# Copyright (C) 2016-2021 Ben Cordero <bencord0@condi.me>
#
# This file is part of blog.condi.me.
#
# blog.condi.me is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# blog.condi.me is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with blog.condi.me.  If not, see <http://www.gnu.org/licenses/>.

from functools import partial

from django.conf.urls import handler404, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.defaults import page_not_found

from graphene_django.views import GraphQLView

import wellknown

import blog.api
import blog.feeds
import blog.views


urlpatterns = [
    re_path(r'^$', blog.views.index, name='index'),
    re_path(r'^about/$', blog.views.about, name='about'),
    re_path(r'^archive/$', blog.views.archive, name='archive'),
    re_path(r'^search/$', blog.views.search, name='search'),
    re_path(r'^health$', blog.views.health, name='health'),
    re_path(r'^feeds/atom/$', blog.feeds.atom, name='atom'),
    re_path(r'^feeds/rss/$', blog.feeds.rss, name='rss'),
    re_path(r'^api/md/(?P<slug>[a-z0-9-_]+)/$', blog.api.md, name='md-slug'),
    re_path(r'^api/(?P<slug>[a-z0-9-_]+)/(?P<item>[a-z][a-z_]+)/$',
            blog.api.item, name='api-item'),
    re_path(r'^api/graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    re_path(r'^api/(?P<slug>[a-z0-9-_]+)/$', blog.api.slug, name='api-slug'),
    re_path(r'^api/$', blog.api.index, name='api-index'),
    re_path(r'^.well-known/keybase.txt$',
            wellknown.keybase, name='wellknown-keybase'),
    re_path(r'^(?P<slug>[a-z0-9-_]+)/$', blog.views.slug, name='slug'),
]

handler404 = partial(page_not_found, template_name='404.html.j2')  # noqa: F811
