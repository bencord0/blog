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

import json
from pathlib import Path
from urllib.parse import urljoin

from django.conf import settings


class ReactLoader:

    @property
    def asset_prefix(self):
        return getattr(settings, 'REACT_LOADER_ASSET_PREFIX', '/')

    def get_assets(self):
        build_folder = getattr(
            settings, 'REACT_LOADER_BUNDLE_DIR', 'src/client/build')
        asset_file = getattr(
            settings, 'REACT_LOADER_ASSET_MANIFEST', 'asset-manifest.json')
        manifest_file = Path(build_folder) / asset_file

        with manifest_file.open() as f:
            return json.load(f)

    def resolve_filepath(self, path):
        files = self.get_assets()['files']
        return urljoin(self.asset_prefix, files[path])

    def scripts(self):
        entrypoints = self.get_assets()['entrypoints']
        for entrypoint in entrypoints:
            if entrypoint.endswith('.js'):
                yield entrypoint
