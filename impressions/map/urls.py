from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.MapListView.as_view(), name='map_list'),
    #url(r'^(?P<slug>\S+)/(?P<chapter_num>\d+)/$', views.ChapterDetailView.as_view(), name='chapter_detail'),
    #url(r'^(?P<slug>\S+)/$', views.StoryDetailView.as_view(), name='story_detail'),
]
