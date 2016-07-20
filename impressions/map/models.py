from django.db import models
from core.models import AssociationMixin
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

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
    # evidence, contexts, people from AssociationMixin
    sites = models.ManyToManyField('map.Site', blank=True)
    # verbose_name='Sites for this layer', 

    def layer_list(self):
        return Layer.objects.all()

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
         
