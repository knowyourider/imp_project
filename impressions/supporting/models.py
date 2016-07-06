from django.db import models
from core.models import ContentType, CommonModel, AssociationMixin

class CommonSupportingModel(CommonModel):
    STATUS_NUMS = (
        (0,'0 - Initial Entry'),
        (1,'1 - Place Holder'),
        (2,'2 - Real Shortname'),
        (3,'3 - Candidate for Publication'),
        (4,'4 - Published'),
    )
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)
    caption = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        abstract = True


class Context(AssociationMixin, CommonSupportingModel):
    CONTEXT_TYPE = (
        ('Background','Background'),
        ('Institution','Institution'),
    )
    CONTEXT_CONTENT_TYPE_ID = 5
    content_type = models.ForeignKey('core.ContentType', 
        default=CONTEXT_CONTENT_TYPE_ID)
    context_type = models.CharField(max_length=24, default='Background', 
        choices=CONTEXT_TYPE)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    # filename = models.CharField(max_length=64, blank=True, default='')
    narrative = models.TextField('Description / Label', blank=True, default='')


class EvidenceType(models.Model):
    """docstring for EvidenceType
    Site admin access only -- not the table for evidence items themselves
    """
    is_document_oriented = models.BooleanField('Document-oriented: can have pages ' + 
        'and or transcripts')
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=16, unique=True)
    ordinal = models.IntegerField('Order in Menu', default=99)

    class Meta:
        ordering = ['ordinal']
        
    def __str__(self):
        return self.title       


class EvidenceItem(AssociationMixin, CommonSupportingModel):
    """
    EvidenceItem
    ContentType is defined in Admin in Core > ContentTypes
    """
    EVIDENCE_CONTENT_TYPE_ID = 4
    content_type = models.ForeignKey('core.ContentType', 
        default=EVIDENCE_CONTENT_TYPE_ID)
    evidence_type = models.ForeignKey('supporting.EvidenceType')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    # filename = models.CharField(max_length=64, blank=True, default='')
    narrative = models.TextField('Description / Label', blank=True, default='')
    creator = models.CharField('maker/author', max_length=64, blank=True, default='')
    creation_year = models.IntegerField(blank=True, null=True)
    dimensions = models.CharField(max_length=128, blank=True, default='')
    materials = models.CharField(max_length=128, blank=True, default='')

    def __str__(self):
        return self.title       


class FastFact(CommonSupportingModel):
    """
    FastFact
    ContentType is defined in Admin in Core > ContentTypes
    """
    FASTFACT_TYPES = (
        ('definition','Definition'),
        ('moreinfo','More Info'),
    )
    FASTFACT_CONTENT_TYPE_ID = 6
    content_type = models.ForeignKey('core.ContentType', 
        default=FASTFACT_CONTENT_TYPE_ID)
    fastfact_type = models.CharField(max_length=32, default='moreinfo', 
        choices=FASTFACT_TYPES)
    title = models.CharField(max_length=128)
    narrative = models.TextField('Description / Label', blank=True, default='')
    has_image = models.BooleanField(default=False)

    def __str__(self):
        return self.title       


class Person(AssociationMixin, CommonSupportingModel):
    PERSON_CONTENT_TYPE_ID = 3
    content_type = models.ForeignKey('core.ContentType', 
        default=PERSON_CONTENT_TYPE_ID)
    first_name = models.CharField(max_length=32, blank=True, default='')
    middle_name = models.CharField(max_length=32, blank=True, default='')
    last_name = models.CharField(max_length=32, blank=True, default='')
    title_prefix = models.CharField(max_length=16, blank=True, default='')
    suffix = models.CharField(max_length=16, blank=True, default='')
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    narrative = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['last_name']


class Place(CommonSupportingModel):
    """
    Place of interest
    ContentType is defined in Admin in Core > ContentTypes
    """
    PLACE_CONTENT_TYPE_ID = 9
    content_type = models.ForeignKey('core.ContentType', 
        default=PLACE_CONTENT_TYPE_ID)
    title = models.CharField(max_length=128)
    narrative = models.TextField('Description / Label', blank=True, default='')
    # has_image = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Place of Interest"

    def __str__(self):
        return self.title       


class Special(CommonSupportingModel):
    """
    Special Features
    ContentType is defined in Admin in Core > ContentTypes
    """
    SPECIAL_TYPES = (
        ('animation','Animation'),
        ('slideshow','Slide Show'),
    )
    SPECIAL_CONTENT_TYPE_ID = 8
    content_type = models.ForeignKey('core.ContentType', 
        default=SPECIAL_CONTENT_TYPE_ID)
    special_type = models.CharField(max_length=32, default='animation', 
        choices=SPECIAL_TYPES)
    title = models.CharField(max_length=128)
    narrative = models.TextField('Description / Label', blank=True, default='')

    class Meta:
        verbose_name = "Special Feature"
        
    def __str__(self):
        return self.title       

