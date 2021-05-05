
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
from datetime import datetime
from pathlib import Path

BASE_DIR = (Path(__file__) / '../..').resolve().absolute()
CODE_FILENAME_EXTENTIONS = {
    '.css',
    '.html',
    '.js',
    '.py',
    '.xml',
}
EXCLUDE_FILES = {
    'bootstrap.min.css',
    'bootstrap.min.js',
    'jquery.min.js',
}

EXCLUDE_DIRECTORIES = {
    '.pytest_cache',
    '.tox',
    'node_modules',
}


def test_copyright_headers():
    current_year = datetime.utcnow().year
    expected_header = f'Copyright (C) 2016-{current_year} '

    for root, dirs, files in os.walk(BASE_DIR):
        # Don't scan excluded directories
        for dirname in dirs:
            if dirname in EXCLUDE_DIRECTORIES:
                dirs.remove(dirname)

        root = Path(root)
        for path in (root / filename for filename in files):
            # Don't scan unknown files
            if path.suffix not in CODE_FILENAME_EXTENTIONS:
                continue

            # Don't scan precompiled dependencies
            if path.name in EXCLUDE_FILES:
                continue

            # Don't scan empty files
            if path.stat().st_size == 0:
                continue

            # .find() returns -1 if not found
            assert path.read_text().find(expected_header) > 0, f'''
Copyright header mismatch:
    Expected: {expected_header}
         For: {path.absolute()}
'''
