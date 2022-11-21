from django import template

register = template.Library()

@register.filter
def get_root_parent(category):
    return str(category).split('>')[0].strip()
