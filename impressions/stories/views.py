from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Story, Chapter

class StoryListView(ListView):
    model = Story
    queryset = Story.objects.filter(status_num__gte=settings.STATUS_LEVEL)
    # context_object_name = 'object_list'
    # template_name = 'stories/story_list.html' 


class StoryDetailView(DetailView):
    model = Story
    # context_object_name = 'object'
    # template_name = 'stories/story_detail.html'

class ChapterDetailView(DetailView):
    """
    Two parameters are sent: slug and chapter_num
    Slug finds the story. From there we just have to find the right chapter
    (We're not going directly by chapter pk, and chapters don't have slugs)
    """
    model = Story
    # context_object_name = 'object'
    template_name = 'stories/chapter_detail.html'

    # get the actual chapter    
    def get_context_data(self, **kwargs):
        # get context
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        # get story object from detail view
        story_object = super(ChapterDetailView, self).get_object()
        # chapter_num will come from parameters
        chapter_num_arg = self.kwargs['chapter_num']
        # get the chapter object
        chapter = get_object_or_404(Chapter, story_id=story_object.id, 
            chapter_num=chapter_num_arg)
        # set the chapter object in the context
        context['chapter'] = chapter
        # We need next and previous chapter numbers for navigation
        # get_next, get_prev set by properties in Chapter model

        return context
    
