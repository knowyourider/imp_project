from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Layer, Site


class MapListView(ListView):
    model = Layer
    # context_object_name = 'object_list'
    template_name = 'map/map.html' 
