from django.contrib import admin

from artifacts.models import Artifact

class ArtifactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['title', 'short_name', 'description']}),
        ('Behind the scenes',   {'fields': ['status_num', 'notes'], 'classes': ['collapse']}),
    ]
    #inlines = [QuestionInline, IdeaInline, PageInline]
    list_display = ('title',  'short_name', 'status_num')
    #list_filter	 = ['augmented'] # , 'edit_date'
    search_fields = ['title', 'short_name']
    #filter_horizontal = ['resourcesets', 'artifacts', 'documents', 'connections','weblinks','biblio', 'essays', 'audiovisuals', 'lectures', 'maps', 'profiles']

admin.site.register(Artifact, ArtifactAdmin)
