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
