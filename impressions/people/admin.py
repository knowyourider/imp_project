from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,            {'fields': ['title_prefix', 'first_name', 'last_name', 
            'suffix', 'slug', 'birth_year', 'death_year',
            'menu_blurb', 'narrative']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal', 'edited_by', 
            'edit_date', 'notes'], 'classes': ['collapse']}),
    ]
    list_display = ('last_name', 'first_name', 'slug', 'status_num')
    #list_filter     = ['augmented'] # , 'edit_date'
    search_fields = ['last_name', 'first_name', 'slug']
    #filter_horizontal = ['resourcesets', 'artifacts']

admin.site.register(Person, PersonAdmin)
