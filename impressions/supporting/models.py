from django.db import models
from django.utils.html import format_html
from core.models import ContentType, CommonModel, AssociationMixin, Source

class CommonSupportingModel(CommonModel):
    STATUS_NUMS = (
        (0,'0 - Initial Entry'),
        (1,'1 - In-progress'),
        (2,'2 - Drafted'),
        (3,'3 - Candidate for Publication'),
        (4,'4 - Published'),
    )
    # source id 1 - "Source not defined"
    source = models.ForeignKey('core.Source', default=1)
    status_num = models.IntegerField(default=0, choices=STATUS_NUMS)
    caption = models.CharField('Image Caption', max_length=255, blank=True, default='')

    class Meta:
        abstract = True


class Context(AssociationMixin, CommonSupportingModel):
    # Context type not currently used. Using topic associations instead
    CONTEXT_TYPE = (
        ('Background','Background'),
        ('Institution','Institution'),
    )
    PRIORITY_NUMS = (
        (1,'1 - highest priority'),
        (2,'2 - important'),
        (3,'3 - nice to have'),
        (5,'5 - TBD'),
        (9,'9 - not using'),
    )
    CONTEXT_CONTENT_TYPE_ID = 5
    content_type = models.ForeignKey('core.ContentType', 
        default=CONTEXT_CONTENT_TYPE_ID)
    context_type = models.CharField(max_length=24, default='Background', 
        choices=CONTEXT_TYPE)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    # filename = models.CharField(max_length=64, blank=True, default='')
    narrative = models.TextField('Description / Label', blank=True, default='')
    map_blurb = models.TextField(blank=True, default='')
    priority_num = models.IntegerField(default=5, choices=PRIORITY_NUMS)
    author = models.CharField(max_length=16, blank=True, default='')
    topics = models.ManyToManyField('supporting.Topic', 
        verbose_name='Topics related to this backdrop', blank=True)

    def topic_list(self):
        topiclist = self.topics.all().values_list('slug', flat=True) 
        return ", ".join(topiclist)

    def image_img(self):
        return format_html('<img src="/static/supporting/context/menupics/' + self.slug + \
                    '.jpg" width="100" height="75"/>')
    image_img.short_description = 'Thumb'
 
    class Meta:
        ordering = ['ordinal']
        verbose_name = "Backdrop"

class Topic(models.Model):
    """docstring for Tag"""
    slug = models.SlugField('Topic short name', max_length=24, unique=True)
    title = models.CharField(max_length=64)
    ordinal = models.IntegerField('Order', default=99)

   # list of contexts with a given topic
    @property
    def context_list(self):
        return self.context_set.all()

    class Meta:
        ordering = ['ordinal']
        verbose_name = "Backdrop Topic/Category"

    def __str__(self):
        return self.title

 
class EvidenceType(models.Model):
    """docstring for EvidenceType
    Site admin access only -- not the table for evidence items themselves
    """
    is_document_oriented = models.BooleanField('Document-oriented: can have pages ' + 
        'and or transcripts')
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=16, unique=True)
    ordinal = models.IntegerField('Order in Menu', default=99)

    class Meta:
        ordering = ['ordinal']
        
    def __str__(self):
        return self.title       


class EvidenceItem(AssociationMixin, CommonSupportingModel):
    """
    EvidenceItem
    ContentType is defined in Admin in Core > ContentTypes
    """
    EVIDENCE_CONTENT_TYPE_ID = 4
    content_type = models.ForeignKey('core.ContentType', 
        default=EVIDENCE_CONTENT_TYPE_ID)
    evidence_type = models.ForeignKey('supporting.EvidenceType')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, default='')
    # filename = models.CharField(max_length=64, blank=True, default='')
    narrative = models.TextField('Description / Label', blank=True, default='')
    creator = models.CharField('maker/author', max_length=64, blank=True, default='')
    creation_year = models.IntegerField(blank=True, null=True)
    is_circa = models.BooleanField(default=False)
    dimensions = models.CharField(max_length=128, blank=True, default='')
    materials = models.CharField(max_length=128, blank=True, default='')
    accession_num = models.CharField(max_length=128, blank=True, default='')
    map_blurb = models.TextField(blank=True, default='')

    def image_img(self):
        return format_html('<img src="/static/supporting/evidenceitem/menupics/' + self.slug + \
                    '.jpg" width="100" height="75"/>')
    image_img.short_description = 'Thumb'

    class Meta:
        ordering = ['ordinal']

    def __str__(self):
        return self.title       


class Page(models.Model):
    """
    Patterned after Slide class
    help_text="File naming: olc/connections/static/connections/audiovisuals/slides/"\
    "short_name_1, short_name_2, etc.")
    """
    evidenceitem = models.ForeignKey('supporting.EvidenceItem')
    page_num = models.IntegerField('page order')
    page_suffix = models.CharField('filename suffix', max_length=64, blank=True, default='')
    page_label = models.CharField('page label', max_length=64, blank=True, default='')
    # image_name = models.CharField('image short name', max_length=32, blank=True, 
    #     default='')
    # caption = models.CharField(max_length=255, blank=True, default='',
    #         help_text="For each page -- Pages ignore Caption at top of form.")
    # source = models.ForeignKey('core.Source', default=1)
    transcript = models.TextField(blank=True, default='',
            help_text="Transcription per page")
         
    """
    # next, prev page, false if none
    def get_next(self):
        next_list = Page.objects.filter(evidenceitem_id=self.evidenceitem_id, 
            page_num__gt=self.page_num)
        if next_list:
            return next_list.first()
        return False

    # Special condition added to prevent going back to page 0 which is the intro
    def get_prev(self):
        prev_list = Page.objects.filter(evidenceitem_id=self.evidenceitem_id, 
            page_num__lt=self.page_num).order_by('-page_num')
        if prev_list:
            prev = prev_list.first()
            if prev.page_num > 0:
                return prev_list.first()
        return False
    """

    class Meta:
        ordering = ['page_num']
        verbose_name = "Document Page"
       
    def __str__(self):
        return self.evidenceitem.slug + "-" + self.page_suffix


class FastFact(CommonSupportingModel):
    """
    FastFact
    ContentType is defined in Admin in Core > ContentTypes
    """
    FASTFACT_TYPES = (
        ('definition','Definition'),
        ('moreinfo','More Info'),
    )
    FASTFACT_CONTENT_TYPE_ID = 6
    content_type = models.ForeignKey('core.ContentType', 
        default=FASTFACT_CONTENT_TYPE_ID)
    fastfact_type = models.CharField(max_length=32, default='moreinfo', 
        choices=FASTFACT_TYPES)
    title = models.CharField(max_length=128)
    narrative = models.TextField('Description / Label', blank=True, default='')
    has_image = models.BooleanField(default=False)

    def image_img(self):
        if self.has_image:
            return format_html('<img src="/static/supporting/fastfact/menupics/' + self.slug + \
                            '.jpg" width="100" height="75"/>')
        else:
            return '(text-only)'
    image_img.short_description = 'Thumb'

    class Meta:
        verbose_name = "In Brief"

    def __str__(self):
        return self.title       


class Person(AssociationMixin, CommonSupportingModel):
    PERSON_LEVEL = (
        (0,'Minor'),
        (1,'Secondary'),
        (2,'Primary'),
        (9,'Not Using'),
    )
    PERSON_CONTENT_TYPE_ID = 3
    content_type = models.ForeignKey('core.ContentType', 
        default=PERSON_CONTENT_TYPE_ID)
    first_name = models.CharField(max_length=32, blank=True, default='')
    middle_name = models.CharField(max_length=32, blank=True, default='')
    last_name = models.CharField(max_length=32, blank=True, default='')
    title_prefix = models.CharField(max_length=16, blank=True, default='')
    suffix = models.CharField(max_length=16, blank=True, default='')
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    narrative = models.TextField(blank=True, default='')
    person_level = models.IntegerField(default=0, choices=PERSON_LEVEL)

    def image_img(self):
        return format_html('<img src="/static/supporting/person/menupics/' + self.slug + \
                    '.jpg" width="60" height="75"/>')
    image_img.short_description = 'Thumb'

    def primary_person_list(self):
        return Person.objects.filter(person_level=2)

    def secondary_person_list(self):
        return Person.objects.filter(person_level=1)

    def minor_person_list(self):
        return Person.objects.filter(person_level=0)

    class Meta:
        ordering = ['last_name']


class Place(CommonSupportingModel):
    """
    Place of interest
    ContentType is defined in Admin in Core > ContentTypes
    """
    PLACE_CONTENT_TYPE_ID = 9
    content_type = models.ForeignKey('core.ContentType', 
        default=PLACE_CONTENT_TYPE_ID)
    title = models.CharField(max_length=128)
    narrative = models.TextField('Description / Label', blank=True, default='')
    # has_image = models.BooleanField(default=False)
    map_blurb = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Place of Interest"

    def __str__(self):
        return self.title       


class Special(CommonSupportingModel):
    """
    Special Features
    ContentType is defined in Admin in Core > ContentTypes
    """
    SPECIAL_TYPES = (
        ('voices','Voices'),
        ('interactive','Interactive'),
        ('looking','Looking &amp; Seeing'),
        ('slideshow','Slideshow'),
        ('then','Then &amp; Now'),
        ('video','Video Story'),
    )
    SPECIAL_CONTENT_TYPE_ID = 8
    content_type = models.ForeignKey('core.ContentType', 
        default=SPECIAL_CONTENT_TYPE_ID)
    special_type = models.CharField(max_length=32, default='animation', 
        choices=SPECIAL_TYPES)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')
    narrative = models.TextField('Narrative / Label', blank=True, default='')
    map_blurb = models.TextField(blank=True, default='')

    def image_img(self):
        return format_html('<img src="/static/supporting/special/menupics/' + self.slug + \
                    '.jpg" width="100" height="75"/>')
    image_img.short_description = 'Thumb'


    class Meta:
        verbose_name = "Special Feature"
        ordering = ['ordinal']
        
    def __str__(self):
        return self.title       


class Slide(models.Model):
    special = models.ForeignKey('supporting.Special')
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
        next_list = Slide.objects.filter(special_id=self.special_id, 
            slide_num__gt=self.slide_num)
        if next_list:
            return next_list.first()
        return False

    # Special condition added to prevent going back to slide 0 which is the intro
    def get_prev(self):
        prev_list = Slide.objects.filter(special_id=self.special_id, 
            slide_num__lt=self.slide_num).order_by('-slide_num')
        if prev_list:
            prev = prev_list.first()
            if prev.slide_num > 0:
                return prev_list.first()
        return False

    class Meta:
        ordering = ['slide_num']
        
    def __str__(self):
        return self.special.slug + "_" + str(self.slide_num) + "_" + self.image_name

