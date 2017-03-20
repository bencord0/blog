import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
    from django.core.management import execute_from_command_line
    from gunicorn.app.wsgiapp import run

    if len(sys.argv) >= 2 and sys.argv[1] == 'manage':
        execute_from_command_line(sys.argv[1:])
    else:
        # Run the webserver
        sys.argv = [sys.argv[0], 'blog.wsgi:application'] + sys.argv[1:]
        print(sys.argv)
        sys.exit(run())


if __name__ == '__main__':
    main()
