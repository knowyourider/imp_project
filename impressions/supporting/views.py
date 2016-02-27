from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import EvidenceItem, Person

class EvidenceItemListView(ListView):
    model = EvidenceItem
    # context_object_name = 'object_list'
    # template_name = 'supporting/evidenceitem_list.html' 

class EvidenceItemDetailView(DetailView):
    model = EvidenceItem
    # context_object_name = 'object'
    # template_name = 'supporting/evidenceitem_detail.html'


class PersonListView(ListView):
    model = Person
    # context_object_name = 'object_list'
    # template_name = 'supporting/person_list.html' 

class PersonDetailView(DetailView):
    model = Person
    # context_object_name = 'object'
    # template_name = 'supporting/person_detail.html'
