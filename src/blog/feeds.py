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

from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

from .models import Entry


class RssBlogFeed(Feed):
    title = 'Fragments Feed'
    link = '/'
    description = 'Fragments: small, unrelated items. sometimes broken.'
    item_author_name = 'Ben Cordero'

    def items(self):
        return Entry.objects.order_by('-date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html

    def item_link(self, item):
        return reverse('slug', kwargs={'slug': item.slug})

    def item_guid(self, item):
        return '/' + item.slug

    def item_updateddate(self, item):
        return item.date

    def item_pubdate(self, item):
        return item.date


class ContentAtom1Feed(Atom1Feed):
    def add_item_elements(self, handler, item):
        super(ContentAtom1Feed, self).add_item_elements(handler, item)
        if item.get('content'):
            handler.addQuickElement(
                'content', item['content'], {'type': 'html'})


class AtomBlogFeed(RssBlogFeed):
    feed_type = ContentAtom1Feed
    feed_guid = 'http://blog.condi.me/feeds/atom/'
    subtitle = RssBlogFeed.description

    item_description = None

    def item_extra_kwargs(self, item):
        return {'content': item.html}


atom = AtomBlogFeed()
rss = RssBlogFeed()
