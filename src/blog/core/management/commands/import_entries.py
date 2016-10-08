import json

from glob import glob
from os.path import abspath, join
from django.core.management.base import BaseCommand

from blog.core.models import Entry
from blog.core.utils import parse_date


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', help='Directory to import entries from')

    def handle(self, *args, **kwargs):
        path = kwargs.get('path', '.')
        path = abspath(path)

        print(path)
        for entry_path in glob(join(path, 'metadata/*.json')):
            with open(entry_path) as p:
               entry = json.loads(p.read())
               process_entry(path, entry)


def process_entry(path, data):
    print(data['slug'])
    entry, _ = Entry.objects.get_or_create(slug=data['slug'])
    entry.date = parse_date(data['date'])
    entry.title = data['title']

    with open(join(path, 'markdown/{}.md'.format(data['slug']))) as md:
        entry.md = md.read()

    entry.save()
