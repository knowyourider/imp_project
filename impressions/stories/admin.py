from django.contrib import admin
from .models import Story, Chapter


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 2
    filter_horizontal = ['people', 'evidence']


class StoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['title', 'subtitle', 'slug',
            'menu_blurb', 'introduction']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes'], 'classes': ['collapse']}),
    ]
    inlines = [ChapterInline]
    list_display = ('title',  'slug', 'status_num')
    #list_filter     = ['augmented'] # , 'edit_date'
    search_fields = ['title', 'slug']

admin.site.register(Story, StoryAdmin)
