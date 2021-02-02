from django import template
from django.utils.safestring import mark_safe
from react_loader.loader import ReactLoader

register = template.Library()


@register.simple_tag
def load_react_style(path):
    loader = ReactLoader()
    style = loader.resolve_filepath(path)

    return mark_safe(f'<link type="text/css" href="{style}" rel="stylesheet" />')


@register.simple_tag
def load_react_scripts():
    loader = ReactLoader()

    return mark_safe(''.join(
        f'<script type="text/javascript" src="{script}"></script>'
        for script in loader.scripts()
    ))
