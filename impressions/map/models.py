from django.db import models
from core.models import AssociationMixin
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
import json


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
    # evidence, contexts, people from AssociationMixin
    sites = models.ManyToManyField('map.Site', blank=True)
    # verbose_name='Sites for this layer', 

    def layer_list(self):
        return Layer.objects.all()

    def overlay_list(self):
        return Overlay.objects.all()

    def site_list(self):

        # info to hand off to JavaScript for map popups
        # get the detail layer object and its list of sites
        site_list = self.sites.all()   

        # use values() to create dictionary-type object so we can iterate
        site_list_of_dicts = site_list.values()

        # To values list Add titles and blurbs from associated supporting records   
        # for-loop version easier to read, works, but comprehension might be faster
        # site_info defined in Sites model
        for idx, row in enumerate(site_list_of_dicts):
            # print('site_list_of_dicts[' + str(idx) + ']: ' + 
            #    site_list_of_dicts[idx]['short_name'] + ' site_info: ' + 
            #    site_list[idx].site_info['title'])
            # print('row id:' + str(row['id']))
            # was: row['site_info'] = site_list[idx].site_info
            # don't depend on index - insure that we get the site info for this row 
            #    in the enumeration
            site_object = Site.objects.get(pk=row['id'])
            # add the corresponding site_info (defined in model) to this row
            row['site_info'] = site_object.site_info
            row['site_type_verbose'] = site_object.site_type_verbose
            #row.update( { "test": "test" } )
        
        # comprehension version
        # first, creat the function that will generate the new value
        # Looks like we can't use assignment inside comprehension. Tabling this
        # site_list_values_plus = [row['site_info'] = site_list[1].site_info for 
        #    row in site_list_values]

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
        

class Site(models.Model):
    """
    Sites contain lat and long and point to evidence, context, place-of-interest
    or special feature
    """
    SITE_TYPES = (
        ('evidenceitem','Evidence'),
        ('context','Context'),
        ('place','Place of Interest'),
        ('special','Special Feature'),
    )
    site_type = models.CharField(max_length=16, choices=SITE_TYPES)
    short_name = models.CharField('Short name of the evidence, context, etc.', max_length=48)
    latitude = models.FloatField(blank=True, null=True,
        help_text="Decimal degrees. Right click on google maps - What's Here.")
    longitude = models.FloatField(blank=True, null=True,
        help_text="Decimal degrees, U.S. negative")

    # return verbose site type
    @property
    def site_type_verbose(self):
        return dict(Site.SITE_TYPES)[self.site_type]

    # return object related to this site
    @property
    def site_info(self):
        suppporting_type = self.site_type
        # retrieve model
        SupportingModel = apps.get_model(app_label="supporting", 
                model_name=suppporting_type)
        # get object (move this outside of property for multiple?)
        try:
            supporting_object = SupportingModel.objects.get(slug=self.short_name)
            # need to convert object to json-type dictionary
            # and get subset using a comprehension
            # http://stackoverflow.com/questions/5352546/
            # best-way-to-extract-subset-of-key-value-pairs-from-python-dictionary-object
            site_info = dict((k, supporting_object.__dict__[k]) for k in ('title', 'map_blurb')) 
            return site_info
        except ObjectDoesNotExist:
            return {'title': 'error on: ' + self.short_name, 'map_blurb': 'no ' + 
                suppporting_type + ' with that short name.'}

    class Meta:
        ordering = ['site_type', 'short_name']

    def __str__(self):
        return self.site_type + ": " + self.short_name
         
