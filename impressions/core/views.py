from django.shortcuts import render
from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'index.html' 


class TeamHomeTemplateView(TemplateView):
    template_name = 'team_index.html' 
