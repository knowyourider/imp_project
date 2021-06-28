from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name="ancillary"

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="ancillary/about.html"), 
    	name='about'),
    path('teachers/', TemplateView.as_view(template_name="ancillary/teachers.html"), 
    	name='teachers'),
    path('further/', TemplateView.as_view(template_name="ancillary/further.html"), 
    	name='further'),
    # url(r'^sites/(?P<slug>\S+)/$', views.layer_sites, name='site_list'),    
    # url(r'^deeper/(?P<slug>\S+)/$', views.MapDeeperView.as_view(), name='map_deeper'),    
    # url(r'^about/(?P<slug>\S+)/$', views.MapAboutView.as_view(), name='about_detail'),    
    # url(r'^$', views.MapDetailView.as_view(), name='map_detail'),
]
