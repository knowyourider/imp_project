from django.contrib import admin
from .models import Context, EvidenceType, EvidenceItem, FastFact, Person, Place, \
    Page, Topic


class ContextAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/narr_mblurb_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'caption', 'source', 'narrative']}),
            # 'map_blurb', 
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts', 'featured_specials']}),
        ('Topics / Categories',   {'fields': ['topics']}),
        ('Behind the scenes',   {'fields': ['priority_num', 'status_num', 'ordinal', 
            'author', 'edited_by', 'edit_date', 'notes']}),
    ]
    list_display = ('title', 'slug', 'image_img', 'topic_list', 'priority_num', 
        'status_num', 'author', 'short_notes')
    list_per_page = 40
    filter_horizontal = ['people', 'evidence', 'contexts', 'topics', 'featured_specials']    
    list_filter     = ['priority_num', 'status_num', 'author'] 
    search_fields = ['title', 'slug']

admin.site.register(Context, ContextAdmin)


class TopicAdmin(admin.ModelAdmin):
    """
    Topics / Categories for Context / Backdrops
    """
    fields = ['title', 'slug', 'ordinal']
    list_display = ('title', 'slug', 'ordinal')

admin.site.register(Topic, TopicAdmin)

class EvidenceTypeAdmin(admin.ModelAdmin):
    """docstring for EvidenceTypeAdmin"""
    fields = ['slug', 'title', 'is_document_oriented', 'ordinal']
    list_display = ('slug', 'title', 'is_document_oriented')
            
admin.site.register(EvidenceType, EvidenceTypeAdmin)


class PageInline(admin.TabularInline):
    model = Page
    extra = 2

class EvidenceItemAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/narr_mblurb_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title', 'slug', 'evidence_type', # 'caption',
            'source','creator', 'dimensions', 'materials', 'creation_year', 'is_circa',
            'accession_num', 'narrative']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts', 'featured_specials']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes', 'map_blurb']}),
    ]
    inlines = [PageInline]
    readonly_fields = ('map_blurb',)
    list_display = ('title', 'slug', 'image_img', 'evidence_type', 'creation_year', 
        'status_num')
    list_per_page = 40
    list_filter     = ['evidence_type', 'status_num'] # , 'edit_date'
    filter_horizontal = ['people', 'evidence', 'contexts', 'featured_specials']    
    search_fields = ['title', 'slug']

admin.site.register(EvidenceItem, EvidenceItemAdmin)


class FastFactAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/fastfact_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title', 'slug', 'fastfact_type', 'has_image',
            'caption', 'source', 'narrative']}),
        # ('View Evidence',   {'fields': ['evidence']}),
        ('Behind the scenes',   {'fields': ['status_num', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    list_display = ('title', 'slug', 'image_img', 'fastfact_type', 'has_image', 'status_num')
    list_per_page = 40
    list_filter     = ['status_num'] 
    # filter_horizontal = ['evidence']    
    search_fields = ['title', 'slug']

admin.site.register(FastFact, FastFactAdmin)


class PersonAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/narr_mblurb_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title_prefix', 'first_name', 'middle_name', 
            'last_name', 'suffix', 'slug', 'birth_year', 'death_year',
            'caption', 'source', 'has_image','narrative']}), #'menu_blurb', 
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts', 'featured_specials']}),
        ('Behind the scenes',   {'fields': ['person_level', 'status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    list_display = ('last_name', 'first_name', 'slug', 'image_img', 'person_level',  
        'status_num', 'has_image')
    list_per_page = 40
    filter_horizontal = ['people', 'evidence', 'contexts', 'featured_specials']    
    list_filter     = ['person_level', 'status_num']
    search_fields = ['last_name', 'first_name', 'slug']

admin.site.register(Person, PersonAdmin)


class PlaceAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/narr_mblurb_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'caption', 'source', 
            'map_blurb', 'latitude', 'longitude']}),
        ('Behind the scenes',   {'fields': ['status_num', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    list_display = ('title', 'slug','latitude', 'longitude', 'truncated_map_blurb', 'status_num')
    list_filter     = ['status_num'] 
    search_fields = ['title', 'slug']

    def truncated_map_blurb(self, obj):
        return obj.map_blurb[:30] + "..."

admin.site.register(Place, PlaceAdmin)
