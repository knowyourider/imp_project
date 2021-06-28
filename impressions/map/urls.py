from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name="map"

urlpatterns = [
    path('', TemplateView.as_view(template_name="map/map_intro.html"), name='map_intro'),

    path('sites/<slug:slug>/', views.layer_sites, name='site_list'),    
    path('deeper/<slug:slug>/', views.MapDeeperView.as_view(), name='map_deeper'),    
    path('about/<slug:slug>/', views.FullMapAboutView.as_view(), name='about_detail'),    
    path('ajax/about/<slug:slug>/', views.MapAboutView.as_view(), name='ajax_about_detail'),    

    path('', views.MapDetailView.as_view(), name='map_detail'),
    path('detail/', views.MapDetailView.as_view(), name='map_detail'),
]
