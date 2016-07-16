from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Layer, Site
import json
from django.core import serializers
#from core.views import SiteListMixin


class MapDetailView(DetailView):
    model = Layer
    # context_object_name = 'object'
    template_name = 'map/map_detail.html' 

    # Get params
    def get_context_data(self, **kwargs):
         # Call the base implementation first to get a context
        context = super(MapDetailView, self).get_context_data(**kwargs)
        # Template already has access to sites.all, but we need to add supporting 
        # info to hand off to JavaScript for map popups
        # get the detail layer object and its list of sites
        site_list = self.object.sites.all()   
        # use values() to create dictionary so we can iterate
        site_values = site_list.values()
        # values() creates a list of dictionaries - same as json
        # don't need to convert
        # sites_json_dict = json.dumps(site_values)
        # for loop version easier to read, works, but comprehension might be faster
        for idx, row in enumerate(site_values):
            row['site_info'] = site_list[idx].site_info
            #row.update( { "test": "test" } )

        # comprehension version
        # first, creat the function that will generate the new value
        # Looks like we can't use assignment inside comprehension. Tabling this
        #site_values_plus = [row['site_info'] = site_list[1].site_info for row in site_values]

        context['site_values'] = site_values

        return context
