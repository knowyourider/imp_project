from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^sites/(?P<slug>\S+)/$', views.layer_sites, name='site_list'),    
    url(r'^deeper/(?P<slug>\S+)/$', views.MapDeeperView.as_view(), name='map_deeper'),    
    url(r'^$', views.MapListView.as_view(), name='map_list'),
]
