from django.contrib import admin
from .models import ContentType

class ContentTypeAdmin(admin.ModelAdmin):
    """docstring for ContentTypeAdmin"""
    fields = ['slug', 'app_namespace', 'singular_title', 'plural_title', 'menu_level', 
    	'ordinal']
    list_display = ('slug', 'id', 'app_namespace', 'singular_title', 'plural_title', 
    	'menu_level', 'ordinal')
            
admin.site.register(ContentType, ContentTypeAdmin)
