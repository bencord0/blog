from jinja2 import Environment, FileSystemLoader

from markdown import Markdown

from blog import settings

_md = Markdown().convert
_j2 = Environment(loader=FileSystemLoader('templates'))


def static(path):
    return settings.STATIC_PREFIX + path


def get_recent_entries(count=10):
    return []


def render_template(template, **context):
    template = _j2.get_template(template)
    return template.render(static=static, **context)
