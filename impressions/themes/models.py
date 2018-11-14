from django.db import models
from core.models import ContentType, CommonModel, AssociationMixin, Source

class Theme(AssociationMixin, CommonModel):
    """
    Theme
    A combination of story and chapter structure
    CommonModel includes slug, menu_blurb, ordinal, notes,
        edited_by, edit_date
    AssociationMixin includes contexts, people, evitence
    """
    STATUS_NUMS = (
        (1,'1 - In Admin Only'),
        (2,'2 - Development (Wireframe)'),
        (3,'3 - Candidate for Publication'),
        (4,'4 - Published'),
    )
    THEME_CONTENT_TYPE_ID = 2
    content_type = models.ForeignKey('core.ContentType', default=THEME_CONTENT_TYPE_ID, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64, blank=True, default='')
    author = models.CharField(max_length=128, blank=True, default='')
    image_name = models.CharField(max_length=32, blank=True, default='')
    narrative = models.TextField(blank=True, default='')
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)
    caption = models.CharField('Image Caption', max_length=255, blank=True, default='')
    source = models.ForeignKey('core.Source', default=1, on_delete=models.CASCADE)
    featured_specials = models.ManyToManyField('special.Feature', 
        verbose_name='Special Features related to this item', blank=True)

    # next, prev theme, false if none
    def get_next(self):
        next = Theme.objects.filter(status_num__gt=1, title__gt=self.title)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Theme.objects.filter(status_num__gt=1, 
            title__lt=self.title).order_by('-title')
        if prev:
            return prev.first()
        return False

    def theme_list(self):
        return Theme.objects.filter(status_num__gt=1)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
