from django.contrib import admin
from .models import Layer, Overlay

class LayerAdmin(admin.ModelAdmin):
    change_form_template = 'map/admin/layer_blurb_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'era_description', 'layer_blurb']}), 
        ('Places of Interest',   {'fields': ['places']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts',
            'featured_specials']}),
        ('Behind the scenes',   {'fields': ['ordinal', 'layer_index']}), #layer_identifier
    ]
    filter_horizontal = ['people', 'evidence', 'contexts', 'places', 'featured_specials']    
    list_display = ('title', 'era_description', 'slug' )

admin.site.register(Layer, LayerAdmin)


class OverlayAdmin(admin.ModelAdmin):
    change_form_template = 'map/admin/map_blurb_change_form.html'
    fields = ['title', 'slug', 'map_blurb', 'layer_index', 'ordinal']
    list_display = ('title', 'slug', 'layer_index', 'ordinal')

admin.site.register(Overlay, OverlayAdmin)
