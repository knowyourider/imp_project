from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Theme

class ThemeListView(ListView):
    model = Theme
    queryset = Theme.objects.filter(status_num__gte=settings.STATUS_LEVEL)
    # context_object_name = 'object_list'
    # template_name = 'themes/theme_list.html' 


class ThemeDetailView(DetailView):
    model = Theme
    # context_object_name = 'object'
    # template_name = 'themes/theme_detail.html'
