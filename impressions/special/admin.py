from django.contrib import admin
from .models import Feature, Frame

class FrameInline(admin.TabularInline):
    model = Frame
    extra = 2

class FeatureAdmin(admin.ModelAdmin):
    change_form_template = 'special/admin/narr_m_mblurb_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'special_type', 'caption', 
            'source', 'menu_blurb', 'description', 'narrative']}),
        ('Behind the scenes',   {'fields': ['status_num', 'is_on_menu', 'ordinal', 
            'edited_by', 'edit_date', 'notes']}),
        ('Img dimensions - Then and Now (and Looking time)',   {'fields': ['img_width', 'img_height'], 
            'classes': ['collapse']}),
    ]
    inlines = [FrameInline]
    list_display = ('title', 'slug', 'image_img', 'special_type', 'on_menu',
        'status_num')
    list_per_page = 40
    list_filter     = ['special_type', 'status_num', 'is_on_menu'] 
    search_fields = ['title', 'slug']

admin.site.register(Feature, FeatureAdmin)

