from django.contrib import admin
from .models import Feature, Frame

class FrameInline(admin.TabularInline):
    model = Frame
    extra = 2

class FeatureAdmin(admin.ModelAdmin):
    change_form_template = 'special/admin/narr_m_mblurb_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'special_type', 'caption', 
            'source', 'menu_blurb', 'map_blurb', 'description', 'narrative']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    inlines = [FrameInline]
    list_display = ('title', 'slug', 'image_img', 'special_type', 'status_num')
    list_per_page = 40
    list_filter     = ['special_type', 'status_num'] 
    search_fields = ['title', 'slug']

admin.site.register(Feature, FeatureAdmin)

