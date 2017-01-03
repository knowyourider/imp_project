from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^sites/(?P<slug>\S+)/$', views.layer_sites, name='site_list'),    
    url(r'^deeper/(?P<slug>\S+)/$', views.MapDeeperView.as_view(), name='map_deeper'),    
    url(r'^about/(?P<layer_index>[0-9]+)/$', views.MapAboutView.as_view(), name='map_about'),    
    # url(r'^$', views.MapListView.as_view(), name='map_list'),
    url(r'^$', views.MapDetailView.as_view(), name='map_detail'),
]
