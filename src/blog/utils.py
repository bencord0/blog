from glob import glob

from jinja2 import Environment, FileSystemLoader

from markdown import Markdown

from blog import settings

_md = Markdown().convert
_j2 = Environment(loader=FileSystemLoader('templates'))


def static(path):
    return settings.STATIC_PREFIX + path


def get_recent_entries(count=10):
    meta = glob("metadata/*.json")
    entries = []

    for m in meta:
        with open(m, 'rb') as f:
            entry = json.load(f)
        entries.append(entry)

    return entries
    return [
        {
            "slug": entry["slug"],
            "title": entry["title"],
            "fuzzy_date": entry["date"],
            "summary": entry["slug"],
        } for entry in entries[:count]
    ]


def render_template(template, **context):
    template = _j2.get_template(template)
    return template.render(static=static, **context)
