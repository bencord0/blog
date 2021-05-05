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

import subprocess

from django.conf import settings
from django.contrib.staticfiles.management.commands.collectstatic import (
    Command as Collectstatic
)


class Command(Collectstatic):
    def handle(self, *args, **kwargs):
        script = (
            ('npm', 'install'),
            ('npm', 'run', 'build'),
        )
        for commands in script:
            exit = subprocess.run(
                commands,
                cwd=settings.CLIENT_DIR,
            )

            # Raise excpetions on error
            exit.check_returncode()

        return super().handle(*args, **kwargs)
