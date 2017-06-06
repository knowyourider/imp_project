from django.contrib import admin
from .models import Theme

class ThemeAdmin(admin.ModelAdmin):
    change_form_template = 'themes/admin/narr_blurb_change_form.html'
    fieldsets = [
        (None,	{'fields': ['title', 'subtitle', 'slug', 'author',  
            'caption', 'source', 'menu_blurb', 'narrative']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts', 
            'featured_specials']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes']}), # , 'classes': ['collapse']
    ]
    filter_horizontal = ['people', 'evidence', 'contexts', 'featured_specials']    
    list_display = ('title',  'slug', 'author', 'ordinal', 'status_num')
    search_fields = ['title', 'slug']

admin.site.register(Theme, ThemeAdmin)

