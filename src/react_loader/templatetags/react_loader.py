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

from django import template
from django.utils.safestring import mark_safe

from react_loader.loader import ReactLoader

register = template.Library()


@register.simple_tag
def load_react_style(path):
    loader = ReactLoader()
    style = loader.resolve_filepath(path)

    return mark_safe(
        f'<link type="text/css" href="{style}" rel="stylesheet" />')


@register.simple_tag
def load_react_scripts():
    loader = ReactLoader()

    return mark_safe(''.join(
        f'<script type="text/javascript" src="{script}"></script>'
        for script in loader.scripts()
    ))
