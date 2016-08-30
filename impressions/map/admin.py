from django.contrib import admin
from .models import Layer, Site

class LayerAdmin(admin.ModelAdmin):
    change_form_template = 'map/admin/layer_blurb_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'era_description', 'layer_blurb']}), 
        ('Sites',   {'fields': ['sites']}),
        ('Related supporting (like Dig Deeper)',   {'fields': ['people', 'evidence', 
            'contexts']}),
        ('Behind the scenes',   {'fields': ['ordinal', 'layer_index']}), #layer_identifier
    ]
    filter_horizontal = ['people', 'evidence', 'contexts', 'sites']    
    list_display = ('title', 'era_description', 'slug', 'layer_index' )

admin.site.register(Layer, LayerAdmin)


class SiteAdmin(admin.ModelAdmin):
    fields = ['site_type', 'short_name', 'latitude', 'longitude']
    list_display = ('short_name', 'site_type', 'latitude', 'longitude')
    list_filter     = ['site_type'] 

admin.site.register(Site, SiteAdmin)
