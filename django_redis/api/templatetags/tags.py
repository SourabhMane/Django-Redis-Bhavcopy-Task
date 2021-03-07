from django import template
register = template.Library()

@register.filter
def unicode_to_decode(val):
    return val.decode("utf-8")
    