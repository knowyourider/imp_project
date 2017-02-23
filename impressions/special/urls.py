from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^feature/$', views.FeatureListView.as_view(), name='feature_list'),

    url(r'^feature/(?P<slug>\S+)/(?P<slide_num_arg>[0-9]+)/$', views.feature_detail, \
        name='feature_detail_slide'),    
    url(r'^feature/(?P<slug>\S+)/$', views.feature_detail, name='feature_detail'),  

    # full page versions of the above 
    # url(r'^fullspecial/(?P<slug>\S+)/(?P<slide_num_arg>[0-9]+)/$', views.special_detail, \
    #     name='fullspecial_detail_slide'),    
    # url(r'^fullspecial/(?P<slug>\S+)/$', views.special_detail, name='fullspecial_detail'),  


    # url(r'^special/(?P<slug>\S+)/$', views.SpecialDetailView.as_view(), name='special_detail'),
    # url(r'^special/find-footprints/(?P<image_name>\S+)/$', views.special_f\ootprint, 
    #     name='special_footprint'),    
    # url(r'^special/(?P<slug>\S+)/(?P<slide_num>\d+)/$', views.SlideDetailView.as_view(), 
    #   name='special_footprint'),
    # url(r'^special/interactive/(?P<slug>\S+)/$', 
    #     views.SlideDetailView.as_view(template_name="supporting/special_detail/interactive.html"), 
    #     name='special_interactive'),
]
