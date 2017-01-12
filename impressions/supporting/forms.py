from django import forms
from .models import EvidenceItem, EvidenceType, Topic
# for organization triming
# from django.db import connection
# import itertools

class ContextSearchForm(forms.Form):
    """
    Patterened after sitewide SearchForms and Lesson search in Mystic
    choices defined by the Python values_list function
    """
    q = forms.CharField(max_length=100, required=False)
    page = forms.IntegerField(required=False)

    # get evidence type list directly from the database
    topics = forms.MultipleChoiceField(
        choices = Topic.objects.all().values_list('slug', 
            'title').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

class EvidenceItemSearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)
    page = forms.IntegerField(required=False)

    # get evidence type list directly from the database
    etypes = forms.MultipleChoiceField(
        choices = EvidenceType.objects.all().values_list('slug', 
            'title').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )
