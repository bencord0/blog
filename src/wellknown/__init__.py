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

from django.conf import settings
from django.http import HttpResponse


def keybase(request):
    content = b''
    code = 404

    if settings.WELLKNOWN_KEYBASE:
        try:
            with open(settings.WELLKNOWN_KEYBASE, 'rb') as f:
                content = f.read()
                code = 200
        except FileNotFoundError:
            pass

    return HttpResponse(
        content,
        content_type='text/plain' if content else None,
        status=code)
