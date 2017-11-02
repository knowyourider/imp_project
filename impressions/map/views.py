from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse
# import json
from django.core import serializers
from .models import Layer, Overlay
from core.views import MobileFullMixin

# class MapListView(ListView):
#     model = Layer
#     # context_object_name = 'object'
#     template_name = 'map/map_list.html' 
#     # model could supply overlay list

class MapDetailView(DetailView):
    """
    Detail view to get the default (first) site location
    This default object directly determines the Dig Deeper list,
    and supplies the slug for the JS script in the template that calls the
    JS function that sets the site list and markers.
    Model supplies site_list_dict
    """
    #model = Layer -- see get_object below
    # context_object_name = 'object'
    template_name = 'map/map_detail.html' 
    # get default layer
    def get_object(self):
        layers = Layer.objects.all()
        return layers[0]


class MapDeeperView(DetailView):
    model = Layer
    # context_object_name = 'object'
    template_name = 'map/_map_deeper.html' 

# class MapAboutView(DetailView):
#   """ this one was for single ajax about box """
#     # model = Overlay
#     # context_object_name = 'object'
#     template_name = 'map/_map_about.html' 
#     def get_object(self):
#         return get_object_or_404(Overlay, layer_index=self.kwargs['layer_index'])


class MapAboutView(MobileFullMixin, DetailView):
    model = Overlay
    # context_object_name = 'object'
    # template_name = 'map/overlay_detail.html' 

class FullMapAboutView(MapAboutView):
    extend_base = 'supporting/base_detail_full.html'
    link_name = 'swapfull_'
    link_class = 'swap_fullpop'


def layer_sites(request, slug):

    # get layer object
    layer_object = get_object_or_404(Layer, slug=slug)

    # layer model has def that creates site list
    site_list_of_dicts = layer_object.site_list()

    # need special return type - can't just return string
    # JsonResponse seems to accept valid string
    return JsonResponse(site_list_of_dicts, safe=False)
