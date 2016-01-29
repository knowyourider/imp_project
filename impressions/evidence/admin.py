from django.contrib import admin
from .models import Artifact

class ArtifactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['title', 'slug', 'description']}),
        ('Behind the scenes',   {'fields': ['status_num', 'notes'], 'classes': ['collapse']}),
    ]
    #inlines = [QuestionInline, IdeaInline, PageInline]
    list_display = ('title',  'slug', 'status_num')
    #list_filter	 = ['augmented'] # , 'edit_date'
    search_fields = ['title', 'slug']
    #filter_horizontal = ['resourcesets', 'artifacts', 'documents', 'connections','weblinks','biblio', 'essays', 'audiovisuals', 'lectures', 'maps', 'profiles']

admin.site.register(Artifact, ArtifactAdmin)
