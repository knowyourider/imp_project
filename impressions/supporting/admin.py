from django.contrib import admin
from .models import Context, EvidenceType, EvidenceItem, FastFact, Person


class ContextAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/context_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'menu_blurb',
             'narrative']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    list_display = ('id', 'title', 'slug', 'status_num')
    filter_horizontal = ['people', 'evidence', 'contexts']    
    list_filter     = ['status_num'] 
    search_fields = ['title', 'slug']

admin.site.register(Context, ContextAdmin)


class EvidenceTypeAdmin(admin.ModelAdmin):
    """docstring for EvidenceTypeAdmin"""
    fields = ['slug', 'title', 'is_document_oriented', 'ordinal']
    list_display = ('slug', 'title', 'is_document_oriented')
            
admin.site.register(EvidenceType, EvidenceTypeAdmin)


class EvidenceItemAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/evidence_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title', 'slug', 'evidence_type',
            'creator', 'dimensions', 'materials', 'creation_year', 'menu_blurb',
            'narrative']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    #inlines = [QuestionInline, IdeaInline, PageInline]
    list_display = ('id', 'title',  'slug', 'evidence_type', 'creation_year', 'status_num')
    list_filter     = ['evidence_type', 'status_num'] # , 'edit_date'
    filter_horizontal = ['people', 'evidence', 'contexts']    
    search_fields = ['title', 'slug']

admin.site.register(EvidenceItem, EvidenceItemAdmin)


class FastFactAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/fastfact_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title', 'slug', 'has_image',
            'narrative']}),
        ('Behind the scenes',   {'fields': ['status_num', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    #inlines = [QuestionInline, IdeaInline, PageInline]
    list_display = ('id', 'title',  'slug', 'has_image')
    list_filter     = ['status_num'] 
    search_fields = ['title', 'slug']

admin.site.register(FastFact, FastFactAdmin)


class PersonAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/person_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title_prefix', 'first_name', 'middle_name', 
            'last_name', 'suffix', 'slug', 'birth_year', 'death_year',
            'menu_blurb', 'narrative']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes']}),
    ]
    list_display = ('id', 'last_name', 'first_name', 'slug', 'status_num')
    filter_horizontal = ['people', 'evidence', 'contexts']    
    #list_filter     = ['augmented'] # , 'edit_date'
    search_fields = ['last_name', 'first_name', 'slug']

admin.site.register(Person, PersonAdmin)
