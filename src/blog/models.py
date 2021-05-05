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

import arrow

from django.db import models
from django.urls import reverse

from markdown import Markdown

_md = Markdown().convert


class Entry(models.Model):
    slug = models.SlugField(primary_key=True, max_length=128)
    title = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    md = models.TextField()

    @property
    def html(self):
        return _md(self.md)

    @property
    def summary(self):
        return self.html.split('</p>', 1)[0]

    @property
    def fuzzy_date(self):
        published = arrow.get(self.date)
        return published.humanize()

    def __str__(self):
        return 'slug={}'.format(self.slug)

    def as_dict(self):
        return {
            'api_url': reverse('api-slug', kwargs={'slug': self.slug}),
            'content': self.md,
            'date': self.date,
            'fuzzy_date': self.fuzzy_date,
            'html': self.html,
            'html_url': reverse('slug', kwargs={'slug': self.slug}),
            'md_url': reverse('md-slug', kwargs={'slug': self.slug}),
            'slug': self.slug,
            'summary': self.summary,
            'title': self.title,
        }

    @property
    def url(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        return reverse('slug', kwargs={'slug': self.slug})
