from django.db import models
from core.models import AssociationMixin
from django.apps import apps


class Layer(AssociationMixin, models.Model):
    """
    Info for each layer
    """
    title = models.CharField(max_length=128)
    layer_identifier = models.CharField(max_length=64, blank=True, default='')  
    layer_blurb = models.TextField(blank=True, default='')
    # evidence, contexts, people from AssociationMixin
    sites = models.ManyToManyField('map.Site', 
        verbose_name='Sites relevant to this layer', blank=True)


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
    )
    site_type = models.CharField(max_length=16, choices=SITE_TYPES)
    short_name = models.CharField('Short name of the evidence, context, etc.', max_length=48)
    latitude = models.FloatField(blank=True, null=True,
        help_text="Decimal degrees. Right click on google maps - What's Here.")
    longitude = models.FloatField(blank=True, null=True,
        help_text="Decimal degrees, U.S. negative")

    # return object related to this site
    @property
    def site_info(self):
        suppporting_type = self.site_type
        # retrieve model
        SupportingModel = apps.get_model(app_label="supporting", 
                model_name=suppporting_type)
        # get object (move this outside of property for multiple?)
        supporting_object = SupportingModel.objects.get(slug=self.short_name)
        # need to convert object to json-type dictionary
        # and get subset using a comprehension
        # http://stackoverflow.com/questions/5352546/
        # best-way-to-extract-subset-of-key-value-pairs-from-python-dictionary-object
        site_info = dict((k, supporting_object.__dict__[k]) for k in ('title', 'narrative')) 
        # and get subset
        return site_info

    def __str__(self):
        return self.site_type + ": " + self.short_name
         