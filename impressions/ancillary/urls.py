from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="ancillary/about.html"), 
    	name='about'),
    url(r'^teachers/$', TemplateView.as_view(template_name="ancillary/teachers.html"), 
    	name='teachers'),
    url(r'^further/$', TemplateView.as_view(template_name="ancillary/further.html"), 
    	name='further'),
    # url(r'^sites/(?P<slug>\S+)/$', views.layer_sites, name='site_list'),    
    # url(r'^deeper/(?P<slug>\S+)/$', views.MapDeeperView.as_view(), name='map_deeper'),    
    # url(r'^about/(?P<slug>\S+)/$', views.MapAboutView.as_view(), name='about_detail'),    
    # url(r'^$', views.MapDetailView.as_view(), name='map_detail'),
]
