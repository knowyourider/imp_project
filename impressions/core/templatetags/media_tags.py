from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def media_url(path):
    """Returns the media URL for a given path."""
    if not path:
        return ''
    # Ensure path doesn't start with a slash
    path = path.lstrip('/')
    return f"{settings.MEDIA_URL}{path}"

@register.simple_tag
def story_image(slug, subdir='menupics'):
    """Helper specifically for story images."""
    return f"{settings.MEDIA_URL}stories/{subdir}/{slug}.jpg"