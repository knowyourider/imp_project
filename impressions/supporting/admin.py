from django.contrib import admin
from .models import Context, EvidenceType, EvidenceItem, Person


class ContextAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/context_change_form.html'
    fieldsets = [
        (None,  {'fields': ['title', 'slug', 'menu_blurb',
             'narrative']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'slug', 'status_num')
    filter_horizontal = ['people', 'evidence', 'contexts']    
    #list_filter     = ['augmented'] # , 'edit_date'
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
            'edit_date', 'notes'], 'classes': ['collapse']}),
    ]
    #inlines = [QuestionInline, IdeaInline, PageInline]
    list_display = ('title',  'slug', 'evidence_type', 'creation_year', 'status_num')
    list_filter     = ['evidence_type'] # , 'edit_date'
    filter_horizontal = ['people', 'evidence', 'contexts']    
    search_fields = ['title', 'slug']

admin.site.register(EvidenceItem, EvidenceItemAdmin)

class PersonAdmin(admin.ModelAdmin):
    change_form_template = 'supporting/admin/person_change_form.html'
    fieldsets = [
        (None,            {'fields': ['title_prefix', 'first_name', 'middle_name', 
            'last_name', 'suffix', 'slug', 'birth_year', 'death_year',
            'menu_blurb', 'narrative']}),
        ('Dig Deeper',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes'], 'classes': ['collapse']}),
    ]
    list_display = ('last_name', 'first_name', 'slug', 'status_num')
    filter_horizontal = ['people', 'evidence', 'contexts']    
    #list_filter     = ['augmented'] # , 'edit_date'
    search_fields = ['last_name', 'first_name', 'slug']

admin.site.register(Person, PersonAdmin)
