from django import template

register = template.Library()


@register.filter
def get_tuple_value(value,arg):
    return value[arg]


@register.filter
def remainder(value, arg):
    return value % arg


@register.filter
def split(value, arg):
    return value.split("-")[arg]
