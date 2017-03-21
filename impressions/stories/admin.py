from django.contrib import admin
from .models import Story, Chapter


class StoryAdmin(admin.ModelAdmin):
    change_form_template = 'stories/admin/story_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title', 'subtitle', 'slug', 'image_name',
            'caption', 'source', 'menu_blurb', 'introduction']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes']}), # , 'classes': ['collapse']
    ]
    list_display = ('title',  'slug', 'ordinal', 'status_num')
    search_fields = ['title', 'slug']

admin.site.register(Story, StoryAdmin)


class ChapterAdmin(admin.ModelAdmin):
    change_form_template = 'stories/admin/chapter_change_form.html'
    fieldsets = [
        (None,  {'fields': ['story', 'chapter_num', 'title', 'image_name',
            'caption', 'source', 'is_vertical', 'narrative', 
            'has_include', 'include_path']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts',
            'featured_specials']}),
    ]
    filter_horizontal = ['people', 'evidence', 'contexts', 'featured_specials']    
    #search_fields = ['title']
    list_display = ('title',  'chapter_num', 'story')
    list_filter     = ['story'] # , 'edit_date'
    search_fields = ['title']

admin.site.register(Chapter, ChapterAdmin)
