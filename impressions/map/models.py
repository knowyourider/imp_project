from django.db import models
from core.models import AssociationMixin


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

    def __str__(self):
        return self.site_type + ": " + self.short_name
         
