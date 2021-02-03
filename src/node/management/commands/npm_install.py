import subprocess

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        exit = subprocess.run(
            ['npm', 'install'],
            cwd=settings.CLIENT_DIR,
        )

        exit.check_returncode()
