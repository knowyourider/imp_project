from django.db import models
from core.models import ContentType, CommonModel

class EvidenceType(models.Model):
    """docstring for EvidenceType"""
    is_document_oriented = models.BooleanField('Document-oriented: can have pages and/or transcripts')
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=16, unique=True)
    ordinal = models.IntegerField('Order in Menu', default=99)

    class Meta:
        ordering = ['ordinal']
        
    def __str__(self):
        return self.title       

class EvidenceItem(CommonModel):
    """
    EvidenceItem
    ContentType is defined in Admin in Core > ContentTypes
    """
    EVIDENCE_CONTENT_TYPE_ID = 4
    content_type = models.ForeignKey('core.ContentType', default=EVIDENCE_CONTENT_TYPE_ID)
    evidence_type = models.ForeignKey('evidence.EvidenceType')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    # filename = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField('Description / Label', blank=True, default='')
    creator = models.CharField('maker/author', max_length=64, blank=True, default='')
    creation_year = models.IntegerField(blank=True, null=True)
    dimensions = models.CharField(max_length=128, blank=True, default='')
    materials = models.CharField(max_length=128, blank=True, default='')


"""
Maybe there's an evidence type table
    fore each evidence_item there's a dropdown for which type it is
    That way type titles can be changed, added.


class EvidenceCommonModel(CommonModel):
    #Abstract class for fields common to Artifacts and Documents
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    # filename = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField('Short Description', blank=True, default='')
    creator = models.CharField('maker/author', max_length=64, blank=True, default='')
    initial_zoom = models.IntegerField('Initial zoom - Default (blank) is 50 (%)', 
        null=True, blank=True)
    initial_x = models.IntegerField('X - Default (blank) is 0 (centered)',null=True, 
        blank=True)
    # initial_y varies between artifacts and documents, so is in model for each.

    class Meta:
        abstract = True


class Artifact(EvidenceCommonModel):
    ARTIFACT_CONTENT_TYPE_ID = 3
    content_type = models.ForeignKey('core.ContentType', default=ARTIFACT_CONTENT_TYPE_ID)
    materials = models.CharField(max_length=128, blank=True, default='')
    measurements = models.CharField(max_length=128, blank=True, default='')
    # init zoom and x are shared from core.
    initial_y = models.IntegerField('Y - Default (blank) is 0 (centered)', null=True, 
        blank=True)
"""

