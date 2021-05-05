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

import os
import sys

try:
    from psycopg2cffi import compat
    compat.register()
except ImportError:
    pass


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    from gunicorn.app.wsgiapp import run

    if len(sys.argv) >= 2 and sys.argv[1] == 'manage':
        execute_from_command_line(sys.argv[1:])
    else:
        # Run the webserver
        sys.argv = [
            sys.argv[0],
            'config.asgi:application',
            '-k', 'uvicorn.workers.UvicornWorker'
        ] + sys.argv[1:]

        print(sys.argv)
        sys.exit(run())


if __name__ == '__main__':
    main()
