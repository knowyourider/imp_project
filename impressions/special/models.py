from django.db import models
from django.utils.html import format_html
from core.models import AssociationMixin, Source # ContentType
from supporting.models import CommonSupportingModel

class Feature(CommonSupportingModel):
    """
    Special Features
    ContentType is defined in Admin in Core > ContentTypes
    """
    SPECIAL_TYPES = (
        ('slideshow','Slideshow'),
        ('video','Video Story'),
        ('voices','Voices'),
        ('looking','Looking &amp; Seeing'),
        ('then','Then &amp; Now'),
        ('footprint','Activity: Footprints'),
        ('explore','Activity: Explore'),
    )
    FEATURE_CONTENT_TYPE_ID = 10
    content_type = models.ForeignKey('core.ContentType', 
        default=FEATURE_CONTENT_TYPE_ID)
    special_type = models.CharField(max_length=32, default='slideshow', 
        choices=SPECIAL_TYPES)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')
    narrative = models.TextField('Narrative / Label', blank=True, default='')
    map_blurb = models.TextField(blank=True, default='')

    # in the case of Activities we want to display only "Activities",
    # not the sub type
    def short_type_display(self):
        return self.get_special_type_display().split(":")[0]

    def image_img(self):
        return format_html('<img src="/static/supporting/special/menupics/' + self.slug + \
                    '.jpg" width="100" height="75"/>')    
    image_img.short_description = 'Thumb'

    class Meta:
        verbose_name = "Special Feature"
        ordering = ['ordinal']
        
    def __str__(self):
        return self.title       


class Frame(models.Model):
    feature = models.ForeignKey('special.Feature')
    slide_num = models.IntegerField()
    """
    help_text="File naming: olc/connections/static/connections/audiovisuals/slides/"\
    "short_name_1, short_name_2, etc.")
    """
    image_name = models.CharField('image short name', max_length=32, blank=True, 
        default='')
    caption = models.CharField(max_length=255, blank=True, default='',
            help_text="For each slide -- Slides ignore Caption at top of form.")
    source = models.ForeignKey('core.Source', default=1)
    narrative = models.TextField(blank=True, default='',
            help_text="caption for each slide -- slides ignore Narrative at top of form.")
    num_correct = models.IntegerField(null=True, blank=True)
         
    # next, prev slide, false if none
    def get_next(self):
        next_list = Frame.objects.filter(special_id=self.special_id, 
            slide_num__gt=self.slide_num)
        if next_list:
            return next_list.first()
        return False

    # Special condition added to prevent going back to slide 0 which is the intro
    def get_prev(self):
        prev_list = Frame.objects.filter(special_id=self.special_id, 
            slide_num__lt=self.slide_num).order_by('-slide_num')
        if prev_list:
            prev = prev_list.first()
            if prev.slide_num > 0:
                return prev_list.first()
        return False

    class Meta:
        ordering = ['slide_num']
        
    def __str__(self):
        return self.feature.slug + "_" + str(self.slide_num) + "_" + self.image_name

