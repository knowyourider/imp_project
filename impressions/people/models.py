from django.db import models
from core.models import ContentType, CommonModel

class Person(CommonModel):
    PERSON_CONTENT_TYPE_ID = 3
    content_type = models.ForeignKey('core.ContentType', default=PERSON_CONTENT_TYPE_ID)
    first_name = models.CharField(max_length=32, blank=True, default='')
    last_name = models.CharField(max_length=32, blank=True, default='')
    title_prefix = models.CharField(max_length=16, blank=True, default='')
    suffix = models.CharField(max_length=16, blank=True, default='')
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)

