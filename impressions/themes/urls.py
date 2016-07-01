from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ThemeListView.as_view(), name='theme_list'),
    url(r'^(?P<slug>\S+)/$', views.ThemeDetailView.as_view(), name='theme_detail'),
]
