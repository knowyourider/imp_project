from django import template
from django.core.files.storage import default_storage
from django.conf import settings


register = template.Library()

@register.filter(name='zoom_exists')
def zoom_exists(filepath):
    # filepath = settings.STATIC_URL + "/supporting/evidenceitem/zooms/" + slug + "/TileGroup0/0-0-0.jpg"

    print("--- filepath: " + filepath)

    if default_storage.exists(filepath):
        # return filepath
        return True
    else:
        return False
        # index = filepath.rfind('/')
        # new_filepath = filepath[:index] + '/image.png'
        # return new_filepath

@register.filter(name='file_exists')
def file_exists(filepath):
    print("--- filepath: " + filepath)
    if default_storage.exists(filepath):
        return filepath
    else:
        index = filepath.rfind('pics/')
        new_filepath = filepath[:index +4] + '/placeholder.jpg'
        return new_filepath
