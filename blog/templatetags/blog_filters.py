from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def strip_html_and_truncate(value, arg):
    """Strips HTML tags and truncates to the specified number of characters."""
    stripped_html = strip_tags(value)
    truncated_text = (stripped_html[:arg] + '...') if len(stripped_html) > arg else stripped_html
    print(truncated_text)
    return truncated_text
