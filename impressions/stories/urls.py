from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.StoryListView.as_view(), name='story_list'),
    url(r'^(?P<slug>\S+)/$', views.StoryDetailView.as_view(), name='story_detail'),
]
