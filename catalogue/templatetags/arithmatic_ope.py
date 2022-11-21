from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def div(value, arg):
    return round(value / arg, 2)


@register.filter
def add(value, arg):
    return value + arg