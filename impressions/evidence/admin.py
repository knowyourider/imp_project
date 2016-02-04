from django.contrib import admin
from .models import EvidenceType, EvidenceItem

class   EvidenceTypeAdmin(admin.ModelAdmin):
    """docstring for EvidenceTypeAdmin"""
    fields = ['slug', 'title', 'is_document_oriented', 'ordinal']
    list_display = ('slug', 'title', 'is_document_oriented')
            
admin.site.register(EvidenceType, EvidenceTypeAdmin)


class EvidenceItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['title', 'subtitle', 'slug', 'evidence_type',
            'creator', 'dimensions', 'materials', 'creation_year', 'menu_blurb',
            'description']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes'], 'classes': ['collapse']}),
    ]
    #inlines = [QuestionInline, IdeaInline, PageInline]
    list_display = ('title',  'slug', 'evidence_type', 'creation_year', 'status_num')
    list_filter     = ['evidence_type'] # , 'edit_date'
    search_fields = ['title', 'slug']
    #filter_horizontal = ['resourcesets', 'artifacts']

admin.site.register(EvidenceItem, EvidenceItemAdmin)
