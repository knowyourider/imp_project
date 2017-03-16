from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^feature/$', views.FeatureListView.as_view(), name='feature_list'),

    
    # url(r'^feature/(?P<slug>\S+)/(?P<slide_num_arg>[0-9]+)/$', views.feature_detail, \
    #     name='feature_detail_slide'),    
    # url(r'^feature/(?P<slug>\S+)/$', views.feature_detail, name='feature_detail'),  

    # # full page versions of the above 
    # url(r'^fullfeature/(?P<slug>\S+)/(?P<slide_num_arg>[0-9]+)/$', views.feature_detail, \
    #     name='fullfeature_detail_slide'),    
    # url(r'^fullfeature/(?P<slug>\S+)/$', views.feature_detail, name='fullfeature_detail'),  

    # CBV approach
    # The first part of each name has to match the corresponding
    # name in special.Feature.special_type, e.g. "video"_detail
    # Applies only to the "staring" names, not subsequent slide details

    # ----------- NON-SLIDE FEATURES ---------

    #  ------ VIDEO ---
    url(r'^video/(?P<slug>\S+)/$', 
        views.VideoDetailView.as_view(), name='video_detail'),

    url(r'^full/video/(?P<slug>\S+)/$', 
        views.FullVideoDetailView.as_view(), name='full_video_detail'),

    #  ------ VOICE ---
    # Should have been voice, singular, but too hard to change now
    url(r'^voices/(?P<slug>\S+)/$', 
        views.VoiceDetailView.as_view(), name='voices_detail'),

    url(r'^full/voices/(?P<slug>\S+)/$', 
        views.FullVoiceDetailView.as_view(), name='full_voices_detail'),

    #  ------ THEN AND NOW ---
    url(r'^then/(?P<slug>\S+)/$', 
        views.ThenDetailView.as_view(), name='then_detail'),

    url(r'^full/then/(?P<slug>\S+)/$', 
        views.FullThenDetailView.as_view(), name='full_then_detail'),

    #  ------ EXPLORE ---
    url(r'^explore/(?P<slug>\S+)/$', 
        views.ExploreDetailView.as_view(), name='explore_detail'),

    url(r'^full/explore/(?P<slug>\S+)/$', 
        views.FullExploreDetailView.as_view(), name='full_explore_detail'),

    # ----------- SLIDE-BASED FEATURES ---------

    #  ------ LOOKING ---
    url(r'^looking/(?P<slug>\S+)/$', 
        views.LookingDetailView.as_view(), name='looking_detail'),

    url(r'^full/looking/(?P<slug>\S+)/$', 
        views.FullLookingDetailView.as_view(), name='full_looking_detail'),

    #  ------ SLIDESHOW ---
    # Zero param must also go to intro. e're dependent on the link_name 
    # Wthat distinguishes full from slim pop, so we can't just use 
    # slideshow_detail (no int param) for the link in nav
    url(r'^slideshow/(?P<slug>\S+)/(?P<slide_num_arg>[0])/$', 
        views.IntroSlideshowDetailView.as_view(), name='slideshow_detail'),

    #  with slide number (other than 0)
    url(r'^slideshow/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.SlideshowDetailView.as_view(), name='slideshow_slide_detail'),

    # default - intro
    url(r'^slideshow/(?P<slug>\S+)/$', 
        views.IntroSlideshowDetailView.as_view(), name='slideshow_detail'),

    # zero version of intro
    url(r'^full/slideshow/(?P<slug>\S+)/(?P<slide_num_arg>[0])/$', 
        views.IntroFullSlideshowDetailView.as_view(), name='slideshow_detail'),

    #  full screen with slide number
    url(r'^full/slideshow/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.FullSlideshowDetailView.as_view(), name='full_slideshow_slide_detail'),

    # full screen default - intro
    url(r'^full/slideshow/(?P<slug>\S+)/$', 
        views.IntroFullSlideshowDetailView.as_view(), name='full_slideshow_detail'),


    #  ------ FOOTPRINTS ---
    # zero version of intro
    url(r'^footprint/(?P<slug>\S+)/(?P<slide_num>[0])/$', 
        views.IntroFootprintDetailView.as_view(), name='footprint_detail'),

    #  with slide number
    url(r'^footprint/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.FootprintDetailView.as_view(), name='footprint_slide_detail'),

    # default - intro
    url(r'^footprint/(?P<slug>\S+)/$', 
        views.IntroFootprintDetailView.as_view(), name='footprint_detail'),

    #  full screen with slide number
    url(r'^full/footprint/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.FullFootprintDetailView.as_view(), name='full_footprint_slide_detail'),

    # full screen default - intro
    url(r'^full/footprint/(?P<slug>\S+)/$', 
        views.IntroFullFootprintDetailView.as_view(), name='full_footprint_detail'),

    #  ------ TEAM ---
    url(r'^team/feature/$', views.TeamFeatureListView.as_view(), \
        name='team_special_list'),

]
