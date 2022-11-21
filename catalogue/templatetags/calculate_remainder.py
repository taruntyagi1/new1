from django import template

register = template.Library()

@register.filter
def get_remainder(forloop_counter):
    remainder = forloop_counter%3
    return remainder