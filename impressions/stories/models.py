from django.db import models
from core.models import ContentType, CommonModel, AssociationMixin, Source

class Story(CommonModel):
    STATUS_NUMS = (
        (0,'0 - Initial Entry'),
        (1,'1 - In Admin Only'),
        (2,'2 - Development (Wireframe)'),
        (3,'3 - Candidate for Publication'),
        (4,'4 - Published'),
    )
    STORY_CONTENT_TYPE_ID = 1
    content_type = models.ForeignKey('core.ContentType', default=STORY_CONTENT_TYPE_ID, on_delete=models.CASCADE)
    title = models.CharField(max_length=48)
    subtitle = models.CharField(max_length=64, blank=True, default='')
    image_name = models.CharField(max_length=32, blank=True, default='')
    introduction = models.TextField(blank=True, default='')
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)
    caption = models.CharField('Image Caption', max_length=255, blank=True, default='')
    source = models.ForeignKey('core.Source', default=1, on_delete=models.CASCADE)

    # next, prev story, false if none
    def get_next(self):
        next = Story.objects.filter(status_num__gt=1, ordinal__gt=self.ordinal)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Story.objects.filter(status_num__gt=1, 
            ordinal__lt=self.ordinal).order_by('-ordinal')
        if prev:
            return prev.first()
        return False

    def story_list(self):
        return Story.objects.filter(status_num__gt=1)

    def chapter_list(self):
        return Chapter.objects.filter(story_id=self.id)

    class Meta:
        ordering = ['ordinal']


class Chapter(AssociationMixin, models.Model):
    story = models.ForeignKey('stories.Story', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    chapter_num = models.IntegerField(default=0)
    image_name = models.CharField(max_length=32, blank=True, default='')
    narrative = models.TextField(blank=True, default='')
    caption = models.CharField('Image Caption', max_length=255, blank=True, default='')
    source = models.ForeignKey('core.Source', default=1, on_delete=models.CASCADE)
    is_vertical = models.BooleanField(default=False)
    has_include = models.BooleanField('Use include instead of image',default=False)
    include_path = models.CharField(max_length=64, blank=True, default='')
    # contexts, people and evidence manys supplied by Association Mixin
    fastfacts = models.ManyToManyField('supporting.FastFact', 
        verbose_name='Fast Facts related to this item', blank=True)
    featured_specials = models.ManyToManyField('special.Feature', 
        verbose_name='Special Features related to this item', blank=True)

    # next chapter, empty if none
    def get_next(self):
        next = Chapter.objects.filter(story_id=self.story_id, 
            chapter_num__gt=self.chapter_num)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Chapter.objects.filter(story_id=self.story_id, 
            chapter_num__lt=self.chapter_num).order_by('-chapter_num')
        if prev:
            return prev.first()
        return False

    class Meta:
        ordering = ['story', 'chapter_num']

    def __str__(self):
        return self.title
