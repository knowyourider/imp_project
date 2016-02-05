from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Story, Chapter

class StoryListView(ListView):
    model = Story
    # context_object_name = 'object_list'
    # template_name = 'stories/story_list.html' 


class StoryDetailView(DetailView):
    model = Story
    # context_object_name = 'object'
    # template_name = 'stories/story_detail.html'

