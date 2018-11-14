from django.conf.urls import url
from . import views

app_name="stories"

urlpatterns = [
    url(r'^$', views.StoryListView.as_view(), name='story_list'),
    url(r'^team/$', 
        views.StoryListView.as_view(template_name="stories/team_story_list.html"), 
    	name='team_story_list'),
    url(r'^team/(?P<slug>\S+)/$', 
        views.StoryDetailView.as_view(template_name="stories/team_story_detail.html"), 
    	name='team_story_detail'),
    url(r'^(?P<slug>\S+)/(?P<chapter_num>\d+)/$', views.ChapterDetailView.as_view(), 
    	name='chapter_detail'),
    url(r'^(?P<slug>\S+)/$', views.StoryDetailView.as_view(), name='story_detail'),
]
