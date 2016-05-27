from django.db import models
from core.models import ContentType, CommonModel, AssociationMixin

class Story(CommonModel):
    STATUS_NUMS = (
        (1,'1 - In Admin Only'),
        (2,'2 - Development (Wireframe)'),
        (3,'3 - Candidate for Publication'),
        (4,'4 - Published'),
    )
    STORY_CONTENT_TYPE_ID = 1
    content_type = models.ForeignKey('core.ContentType', default=STORY_CONTENT_TYPE_ID)
    title = models.CharField(max_length=48)
    subtitle = models.CharField(max_length=64, blank=True, default='')
    image_name = models.CharField(max_length=32, blank=True, default='')
    introduction = models.TextField(blank=True, default='')
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)

    class Meta:
        ordering = ['title']


class Chapter(AssociationMixin, models.Model):
    story = models.ForeignKey('stories.Story')
    title = models.CharField(max_length=64)
    chapter_num = models.CharField(max_length=8)
    image_name = models.CharField(max_length=32, blank=True, default='')
    narrative = models.TextField(blank=True, default='')
    
    class Meta:
        ordering = ['story', 'chapter_num']

    def __str__(self):
        return self.title
