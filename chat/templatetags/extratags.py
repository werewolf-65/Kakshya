from django import template

register = template.Library()

@register.filter()
def strip_double_quotes(q_string):
    return q_string.replace('"','')
