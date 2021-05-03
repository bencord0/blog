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
