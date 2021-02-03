import subprocess

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
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
