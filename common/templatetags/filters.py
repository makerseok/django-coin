from django import template

register = template.Library()


@register.filter
def tuple0(value):
    return value[0]


@register.filter
def tuple1(value):
    return value[1]


@register.filter
def remainder(value, arg):
    return value % arg


@register.filter
def split(value, arg):
    return value.split("-")[arg]
