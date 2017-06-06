from django.db import models
from core.models import AssociationMixin
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
import json
# from django.core import serializers
# from django.http import JsonResponse

class Layer(AssociationMixin, models.Model):
    """
    Info for each layer
    """
    title = models.CharField(max_length=128)
    slug = models.SlugField('Layer short name', max_length=32, unique=True)
    era_description = models.CharField(max_length=128, blank=True, default='')  
    layer_blurb = models.TextField(blank=True, default='')
    layer_identifier = models.CharField(max_length=64, blank=True, default='')  
    layer_index = models.IntegerField('Base layer index', default=0)
    ordinal = models.IntegerField('List order', default=99)
    # evidence, contexts, people from AssociationMixin -- for dig deeper
    # sites = models.ManyToManyField('map.Site', blank=True)
    places = models.ManyToManyField('supporting.Place', blank=True) # for markers
    featured_specials = models.ManyToManyField('special.Feature', 
        verbose_name='Special Features related to this item', blank=True)

    def layer_list(self):
        return Layer.objects.all()

    # hard code the exclusion of the glacer layer as it needs custom layout
    def overlay_list(self):
        return Overlay.objects.filter(ordinal__lt=9)

    def site_list(self):
        # info to hand off to JavaScript for map popups
        # get the detail layer object and its list of sites
        site_list = self.places.all()   
        # use values() to create "flat" dictionary (excluding sub-lists)
        site_list_of_dicts = site_list.values('slug', 'title', 'map_blurb', 'latitude', 
            'longitude')

        # site_list_of_dicts is actually a ValuesQuerySet
        # so we need to turn it into an actual list
        # and then use json.dumps to create json from list
        return json.dumps(list(site_list_of_dicts))

    class Meta:
        verbose_name = "Location Set"
        ordering = ['ordinal']

    def __str__(self):
        return self.title

class Overlay(models.Model):
    """
    Mainly for blurb to accompany each overlay
    """
    title = models.CharField(max_length=128)
    slug = models.SlugField('Overlay short name', max_length=32, unique=True)
    map_blurb = models.TextField(blank=True, default='')
    ordinal = models.IntegerField('List order', default=99)
    layer_index = models.IntegerField('Overlay layer index', default=0)

    # short goal description
    @property
    def short_blurb(self):
        cutoff = 65
        display_string = self.map_blurb
        if len(display_string) > cutoff:
            return display_string[:cutoff] + "..."
        else:
            return display_string
        
    class Meta:
        # verbose_name = "Overlays"
        ordering = ['ordinal']

    def __str__(self):
        return self.title
        
