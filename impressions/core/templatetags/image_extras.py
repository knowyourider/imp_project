from django import template
from django.core.files.storage import default_storage
from django.conf import settings


register = template.Library()

@register.filter(name='zoom_exists')
def zoom_exists(filepath):
    # filepath = settings.STATIC_URL + "/supporting/evidenceitem/zooms/" + slug + "/TileGroup0/0-0-0.jpg"

    # print("--- filepath: " + filepath)

    if default_storage.exists(filepath):
        # return filepath
        return True
    else:
        return False
        # index = filepath.rfind('/')
        # new_filepath = filepath[:index] + '/image.png'
        # return new_filepath

@register.filter(name='supporting_image_exists')
def file_exists(filepath):
    full_filepath = settings.BASE_DIR + '/supporting/static/supporting/' + filepath # + '.jpg'
    # print("--- filepath: " + filepath)
    # print("--- full_filepath: " + full_filepath)
    if default_storage.exists(full_filepath):
        return filepath
    else:
        index = filepath.rfind('pics/')
        new_filepath = filepath[:index +4] + '/placeholder.jpg'
        return new_filepath


@register.filter(name='supporting_image_truefalse')
def file_exists(filepath):
    full_filepath = settings.BASE_DIR + '/supporting/static/supporting/' + filepath # + '.jpg'
    # print("--- filepath: " + filepath)
    # print("--- full_filepath: " + full_filepath)
    return default_storage.exists(full_filepath)


# Not used
@register.filter(name='file_exists')
def file_exists(filepath):
    full_filepath = settings.STATIC_ROOT + '/' + filepath
    # print("--- full_filepath: " + full_filepath)
    if default_storage.exists(full_filepath):
        return filepath
    else:
        index = filepath.rfind('pics/')
        new_filepath = filepath[:index +4] + '/placeholder.jpg'
        return new_filepath
