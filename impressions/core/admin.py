from django.contrib import admin
from .models import ContentType, Source

class ContentTypeAdmin(admin.ModelAdmin):
    """docstring for ContentTypeAdmin"""
    fields = ['slug', 'app_namespace', 'singular_title', 'plural_title', 'menu_level', 
    	'ordinal']
    list_display = ('slug', 'id', 'app_namespace', 'singular_title', 'plural_title', 
    	'menu_level', 'ordinal')
            
admin.site.register(ContentType, ContentTypeAdmin)


class SourceAdmin(admin.ModelAdmin):
    change_form_template = 'core/admin/notes_change_form.html'
    fieldsets = [
        (None,  {'fields': ['institution', 'slug']}),
        ('Behind the scenes',   {'fields': ['contact', 'notes']}),
    ]
    list_display = ('institution', 'slug', 'contact')
    #filter_horizontal = ['people', 'evidence', 'contexts']    
    search_fields = ['institution', 'slug']

admin.site.register(Source, SourceAdmin)


