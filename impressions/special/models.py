from django.db import models
from django.utils.html import format_html
from django.conf import settings
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
        ('discoverers','Whose Discovery'),
        ('society','Activity: Ladies Literary Society'),
    )
    FEATURE_CONTENT_TYPE_ID = 10
    content_type = models.ForeignKey('core.ContentType', 
        default=FEATURE_CONTENT_TYPE_ID, on_delete=models.CASCADE)
    special_type = models.CharField(max_length=32, default='slideshow', 
        choices=SPECIAL_TYPES)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')
    narrative = models.TextField('Narrative / Label', blank=True, default='')
    map_blurb = models.TextField(blank=True, default='')
    is_on_menu = models.BooleanField('Show on Special Features Menu', default=True)
    img_width = models.IntegerField('img width (or runtime)', blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)

    # for menu - each type a separate list
    def slideshow_list(self):
        return Feature.objects.filter(status_num__gte=settings.STATUS_LEVEL, 
            is_on_menu=True, special_type='slideshow')

    def video_list(self):
        return Feature.objects.filter(status_num__gte=settings.STATUS_LEVEL, 
            is_on_menu=True, special_type='video')

    def voices_list(self):
        return Feature.objects.filter(status_num__gte=settings.STATUS_LEVEL, 
            is_on_menu=True, special_type='voices')

    def looking_list(self):
        return Feature.objects.filter(status_num__gte=settings.STATUS_LEVEL, 
            is_on_menu=True, special_type='looking')

    def then_list(self):
        return Feature.objects.filter(status_num__gte=settings.STATUS_LEVEL, 
            is_on_menu=True, special_type='then')

    # in the case of Activities we want to display only "Activities",
    # not the sub type
    def short_type_display(self):
        return self.get_special_type_display().split(":")[0]

    def image_img(self):
        return format_html('<img src="/static/special/menupics/' + self.slug + \
                    '.jpg" width="100" height="75"/>')    
    image_img.short_description = 'Thumb'

    def on_menu(self):
        # short name for display list
        return self.is_on_menu
    on_menu.short_description = 'menu'
    on_menu.boolean = True

    class Meta:
        verbose_name = "Special Feature"
        ordering = ['special_type', 'ordinal']
        
    def __str__(self):
        return str(self.status_num) + " - " + self.special_type + ": " + self.title


class Frame(models.Model):
    feature = models.ForeignKey('special.Feature', on_delete=models.CASCADE)
    slide_num = models.IntegerField()
    """
    help_text="File naming: olc/connections/static/connections/audiovisuals/slides/"\
    "short_name_1, short_name_2, etc.")
    """
    image_name = models.CharField('image short name', max_length=32, blank=True, 
        default='')
    caption = models.CharField(max_length=255, blank=True, default='',
            help_text="For each slide -- Slides ignore Caption at top of form.")
    source = models.ForeignKey('core.Source', default=1, on_delete=models.CASCADE)
    narrative = models.TextField(blank=True, default='',
            help_text="caption for each slide -- slides ignore Narrative at top of form.")
    num_correct = models.IntegerField(null=True, blank=True)
         
    # next, prev slide, false if none
    def get_next(self):
        next_list = Frame.objects.filter(feature_id=self.feature_id, 
            slide_num__gt=self.slide_num)
        if next_list:
            return next_list.first()
        return False

    # Special condition added to prevent going back to slide 0 which is the intro
    def get_prev(self):
        prev_list = Frame.objects.filter(feature_id=self.feature_id, 
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

