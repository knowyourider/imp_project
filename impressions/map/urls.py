from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name="map"

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="map/map_intro.html"), name='map_intro'),

    url(r'^sites/(?P<slug>\S+)/$', views.layer_sites, name='site_list'),    
    url(r'^deeper/(?P<slug>\S+)/$', views.MapDeeperView.as_view(), name='map_deeper'),    
    url(r'^about/(?P<slug>\S+)/$', views.FullMapAboutView.as_view(), name='about_detail'),    
    url(r'^ajax/about/(?P<slug>\S+)/$', views.MapAboutView.as_view(), name='ajax_about_detail'),    

    url(r'^$', views.MapDetailView.as_view(), name='map_detail'),
    url(r'^detail/$', views.MapDetailView.as_view(), name='map_detail'),
]
