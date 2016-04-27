from django.contrib import admin
from .models import Layer, Site

class LayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['title', 'layer_identifier', 'layer_blurb']}),
        ('Sites',   {'fields': ['sites']}),
        ('Relates supporting (like Dig Deeper)',   {'fields': ['people', 'evidence', 'contexts']}),
    ]
    filter_horizontal = ['people', 'evidence', 'contexts', 'sites']    
    list_display = ('title', 'layer_identifier', 'layer_blurb')

admin.site.register(Layer, LayerAdmin)


class SiteAdmin(admin.ModelAdmin):
    fields = ['site_type', 'short_name', 'latitude', 'longitude']
    list_display = ('short_name', 'site_type', 'latitude', 'longitude')
    list_filter     = ['site_type'] 

admin.site.register(Site, SiteAdmin)
