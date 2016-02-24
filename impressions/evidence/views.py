from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import EvidenceItem

class EvidenceItemListView(ListView):
    model = EvidenceItem
    # context_object_name = 'object_list'
    # template_name = 'evicence/evidenceitem_list.html' 

class EvidenceItemDetailView(DetailView):
    model = EvidenceItem
    # context_object_name = 'object'
    # template_name = 'evicence/evidenceitem_detail.html'
