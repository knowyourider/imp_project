from django.db import models
import datetime

class ContentType(models.Model):
    """docstring for ContentType"""
    slug = models.SlugField('Content type short name', max_length=16, unique=True)
    app_namespace = models.CharField(max_length=16)
    singular_title = models.CharField(max_length=32, blank=True, default='')
    plural_title = models.CharField(max_length=32, blank=True, default='')
    
class CommonModel(models.Model):
    """
    Abstract class for fields common to Artifacts, Documents,
    Maps, Lecture, Project, Resourceset
    """
    STATUS_NUMS = (
        (1,'1 - Entered'),
        (2,'2 - TBD'),
        (3,'3 - Work in progress'),
        (4,'4 - Published'),
    )
    slug = models.SlugField('short name', max_length=48, unique=True)
    menu_blurb = models.TextField(blank=True, default='')
    ordinal = models.IntegerField('Order in Menu', default=99)
    notes = models.TextField('Production Notes', blank=True, default='')
    edited_by = models.CharField(max_length=64, blank=True, default='')
    edit_date = models.DateTimeField('edit date', default=datetime.datetime.now)
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug
