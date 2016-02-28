from django.db import models
from core.models import ContentType, CommonModel, AssociationMixin

class Story(CommonModel):
    STORY_CONTENT_TYPE_ID = 1
    content_type = models.ForeignKey('core.ContentType', default=STORY_CONTENT_TYPE_ID)
    title = models.CharField(max_length=48)
    subtitle = models.CharField(max_length=64, blank=True, default='')
    introduction = models.TextField(blank=True, default='')


class Chapter(AssociationMixin, models.Model):
    story = models.ForeignKey('stories.Story')
    title = models.CharField(max_length=64)
    chapter_num = models.IntegerField()
    narrative = models.TextField(blank=True, default='')
    
    class Meta:
        ordering = ['story', 'chapter_num']

    def __str__(self):
        return self.title
