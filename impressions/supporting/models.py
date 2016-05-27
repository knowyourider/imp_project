from django.db import models
from core.models import ContentType, CommonModel, AssociationMixin

class CommonSupportingModel(CommonModel):
    STATUS_NUMS = (
        (1,'1 - Place Holder'),
        (2,'2 - Real Shortname'),
        (3,'3 - Candidate for Publication'),
        (4,'4 - Published'),
    )
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)

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
    """docstring for EvidenceType"""
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


class FastFact(CommonSupportingModel):
    """
    FastFact
    ContentType is defined in Admin in Core > ContentTypes
    """
    FASTFACT_CONTENT_TYPE_ID = 6
    content_type = models.ForeignKey('core.ContentType', 
        default=FASTFACT_CONTENT_TYPE_ID)
    title = models.CharField(max_length=128)
    narrative = models.TextField('Description / Label', blank=True, default='')
    has_image = models.BooleanField(default=False)


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
        
