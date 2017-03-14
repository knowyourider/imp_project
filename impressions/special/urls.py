from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^feature/$', views.FeatureListView.as_view(), name='feature_list'),

    url(r'^feature/(?P<slug>\S+)/(?P<slide_num_arg>[0-9]+)/$', views.feature_detail, \
        name='feature_detail_slide'),    
    url(r'^feature/(?P<slug>\S+)/$', views.feature_detail, name='feature_detail'),  

    # full page versions of the above 
    url(r'^fullfeature/(?P<slug>\S+)/(?P<slide_num_arg>[0-9]+)/$', views.feature_detail, \
        name='fullfeature_detail_slide'),    
    url(r'^fullfeature/(?P<slug>\S+)/$', views.feature_detail, name='fullfeature_detail'),  

    # CBV approach

    # Video
    url(r'^video/(?P<slug>\S+)/$', 
        views.SimpleFeatureDetailView.as_view(template_name="special/video.html"), 
        name='video_detail'),
    url(r'^full/video/(?P<slug>\S+)/$', 
        views.SimpleFeatureDetailView.as_view(template_name="special/video.html", 
            extend_base = 'supporting/base_detail_full.html'), name='full_video_detail'),

    #  ------ Slideshow
    #  with slide number
    url(r'^slideshow/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.SlideFeatureDetailView.as_view(template_name="special/slideshow.html", 
        link_name = 'slideshow_detail'), # link_class 'swap_pop'is a default
        name='slideshow_detail'),
    # default - intro
    url(r'^slideshow/(?P<slug>\S+)/$', 
        views.SlideFeatureDetailView.as_view(template_name="special/slideshow_intro.html", 
        link_name = 'slideshow_detail'), # link_class 'swap_pop'is a default
        name='slideshow_intro_detail'),
    #  full screen with slide number
    url(r'^full/slideshow/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.SlideFeatureDetailView.as_view(template_name="special/slideshow.html",
        extend_base = 'supporting/base_detail_full.html', 
        link_name = 'slideshow_detail_full', link_class = 'noclass'), 
        name='slideshow_detail_full'),
    # full screen default - intro
    url(r'^full/slideshow/(?P<slug>\S+)/$', 
        views.SlideFeatureDetailView.as_view(template_name="special/slideshow_intro.html",
        extend_base = 'supporting/base_detail_full.html', 
        link_name = 'slideshow_detail_full', link_class = 'noclass'), 
        name='slideshow_intro_full_detail'),

]
