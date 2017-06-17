from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

class HomeTemplateView(TemplateView):
    # template_name = 'index.html' 

    # Temporarily handle comming soon vs. regular home page
    if settings.SITE_ID == 2:
        template_name = 'index-coming.html' 
    else:
        # regular home page
        template_name = 'index.html' 


class TeamHomeTemplateView(TemplateView):
    template_name = 'team_index.html' 
