from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse
# import json
from django.core import serializers
from .models import Layer, Site


class MapDetailView(DetailView):
    #model = Layer
    # context_object_name = 'object'
    template_name = 'map/map_detail.html' 
    # model supplies site_list_dict
    # get default layer
    def get_object(self):
        return get_object_or_404(Layer, slug='fossils')


class MapDeeperView(DetailView):
    model = Layer
    # context_object_name = 'object'
    template_name = 'map/_map_deeper.html' 


def layer_sites(request, slug):

    # get layer object
    layer_object = get_object_or_404(Layer, slug=slug)

    # layer model has def that creates site list
    site_list_of_dicts = layer_object.site_list()

    # need special return type - can't just return string
    # JsonResponse seems to accept valid string
    return JsonResponse(site_list_of_dicts, safe=False)
