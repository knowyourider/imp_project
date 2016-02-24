from django.shortcuts import render, get_object_or_404
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

class ChapterDetailView(DetailView):
    """
    Two parameters are sent: slug and chapter_num
    Slug finds the story. From there we just have to find the right chapter
    """
    model = Story
    # context_object_name = 'object'
    template_name = 'stories/chapter_detail.html'
    # get data for this menu type
    
    def get_context_data(self, **kwargs):
        # get context
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        # get story object from detail view
        self.object = super(ChapterDetailView, self).get_object()
        # chapter_num will come from parameters
        # chapter_num = self.kwargs['chapter_num']
        # get the chapter object
        chapter = get_object_or_404(Chapter, story_id=self.object.id, chapter_num=self.kwargs['chapter_num'])
        # set the context
        context['chapter'] = chapter
        return context
    
