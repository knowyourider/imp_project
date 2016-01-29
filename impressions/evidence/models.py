from django.db import models
from core.models import CommonModel

class EvidenceCommonModel(CommonModel):
    """
    Abstract class for fields common to Artifacts and Documents
    """
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    # filename = models.CharField(max_length=64, blank=True, default='')
    description = models.TextField('Short Description', blank=True, default='')
    creator = models.CharField('maker/author', max_length=64, blank=True, default='')
    initial_zoom = models.IntegerField('Initial zoom - Default (blank) is 50 (%)', null=True, blank=True)
    initial_x = models.IntegerField('X - Default (blank) is 0 (centered)',null=True, blank=True)
    # initial_y varies between artifacts and documents, so is in model for each.

    class Meta:
        abstract = True


class Artifact(EvidenceCommonModel):
    materials = models.CharField(max_length=128, blank=True, default='')
    measurements = models.CharField(max_length=128, blank=True, default='')
    # init zoom and x are shared from core.
    initial_y = models.IntegerField('Y - Default (blank) is 0 (centered)', null=True, 
        blank=True)

