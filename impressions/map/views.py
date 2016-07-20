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
        site_list_dict = site_list.values()

        print('site_list_dict: ' + str(site_list_dict))

        # values() creates a list of dictionaries - same as json -- don't need to convert
        # the conversion not needed: sites_json_dict = json.dumps(site_list_dict)
        # for-loop version easier to read, works, but comprehension might be faster
        # site_info defined in Sites model
        for idx, row in enumerate(site_list_dict):
            # print('site_list_dict[' + str(idx) + ']: ' + site_list_dict[idx]['short_name'] + ' site_info: ' + site_list[idx].site_info['title'])
            # print('row id:' + str(row['id']))
            # was: row['site_info'] = site_list[idx].site_info
            # don't depend on index - insure that we get the site info for this row in the enumeration
            site_object = Site.objects.get(pk=row['id'])
            # add the corresponding site_info (defined in model) to this row
            row['site_info'] = site_object.site_info
            row['site_type_verbose'] = site_object.site_type_verbose
            #row.update( { "test": "test" } )

        # comprehension version
        # first, creat the function that will generate the new value
        # Looks like we can't use assignment inside comprehension. Tabling this
        #site_list_dict_plus = [row['site_info'] = site_list[1].site_info for row in site_list_dict]

        context['site_values'] = site_list_dict

        return context
