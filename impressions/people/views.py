from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Person

class PersonListView(ListView):
    model = Person
    # context_object_name = 'object_list'
    # template_name = 'people/person_list.html' 

