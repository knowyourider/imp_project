from django.db import models
from core.models import ContentType, CommonModel

class Story(CommonModel):
    STORY_CONTENT_TYPE_ID = 1
    content_type = models.ForeignKey('core.ContentType', default=STORY_CONTENT_TYPE_ID)
    title = models.CharField(max_length=48)
    subtitle = models.CharField(max_length=64, blank=True, default='')
    introduction = models.TextField(blank=True, default='')


class Chapter(models.Model):
    story = models.ForeignKey('stories.Story')
    title = models.CharField(max_length=64)
    chapter_num = models.IntegerField()
    narrative = models.TextField(blank=True, default='')
    #people = models.ManyToManyField('people.Person', 
    #    verbose_name='People related to this chapter', blank=True)
    #evidence = models.ManyToManyField('evidence.EvidenceItem', 
    #    verbose_name='evidence items related to this chapter', blank=True)
    
    class Meta:
        ordering = ['story', 'chapter_num']

    def __str__(self):
        return self.title
