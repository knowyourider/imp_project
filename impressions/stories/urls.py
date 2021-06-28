from django.urls import path
from . import views

app_name="stories"

urlpatterns = [
    path('', views.StoryListView.as_view(), name='story_list'),
    path('team/', 
        views.StoryListView.as_view(template_name="stories/team_story_list.html"), 
    	name='team_story_list'),
    path('team/<slug:slug>/', 
        views.StoryDetailView.as_view(template_name="stories/team_story_detail.html"), 
    	name='team_story_detail'),
    path('<slug:slug>/<chapter_num>/', views.ChapterDetailView.as_view(), 
    	name='chapter_detail'),
    path('<slug:slug>/', views.StoryDetailView.as_view(), name='story_detail'),
]
