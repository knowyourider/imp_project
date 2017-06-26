from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^feature/$', views.FeatureListView.as_view(), name='feature_list'),

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

    url(r'^swapfull/video/(?P<slug>\S+)/$', 
        views.SwapFullVideoDetailView.as_view(), name='swapfull_video_detail'),

    #  ------ VOICE ---
    # Should have been voice, singular, but too hard to change now
    url(r'^voices/(?P<slug>\S+)/$', 
        views.VoiceDetailView.as_view(), name='voices_detail'),

    url(r'^full/voices/(?P<slug>\S+)/$', 
        views.FullVoiceDetailView.as_view(), name='full_voices_detail'),

    url(r'^swapfull/voices/(?P<slug>\S+)/$', 
        views.SwapFullVoiceDetailView.as_view(), name='swapfull_voices_detail'),

    #  ------ EXPLORE ---
    url(r'^explore/(?P<slug>\S+)/$', 
        views.ExploreDetailView.as_view(), name='explore_detail'),

    url(r'^full/explore/(?P<slug>\S+)/$', 
        views.FullExploreDetailView.as_view(), name='full_explore_detail'),

    url(r'^swapfull/explore/(?P<slug>\S+)/$', 
        views.SwapFullExploreDetailView.as_view(), name='swapfull_explore_detail'),

    #  ------ DICOVERERS ---
    # Not stand-alone -- only serves voting in Whose Discovery, Chapter 8
    url(r'^discoverers/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.DiscoverersDetailView.as_view(), name='discoverers_detail'),

    # ----------- SLIDE-BASED FEATURES ---------

    #  ------ THEN AND NOW ---
    url(r'^then/(?P<slug>\S+)/$', 
        views.ThenDetailView.as_view(), name='then_detail'),

    url(r'^full/then/(?P<slug>\S+)/$', 
        views.FullThenDetailView.as_view(), name='full_then_detail'),

    url(r'^swapfull/then/(?P<slug>\S+)/$', 
        views.SwapFullThenDetailView.as_view(), name='swapfull_then_detail'),

    #  ------ LOOKING ---
    url(r'^looking/(?P<slug>\S+)/$', 
        views.LookingDetailView.as_view(), name='looking_detail'),

    url(r'^full/looking/(?P<slug>\S+)/$', 
        views.FullLookingDetailView.as_view(), name='full_looking_detail'),

    url(r'^swapfull/looking/(?P<slug>\S+)/$', 
        views.SwapFullLookingDetailView.as_view(), name='swapfull_looking_detail'),


    #  ------ SLIDESHOW ---
    # Zero param must also go to intro. We're dependent on the link_name 
    # which distinguishes full from slim pop, so we can't just use 
    # slideshow_detail (no int param) for the link in nav
    url(r'^slideshow/(?P<slug>\S+)/(?P<slide_num_arg>[0])/$', 
        views.IntroSlideshowDetailView.as_view(), name='reintro-slideshow_detail'),

    #  with slide number (other than 0)
    url(r'^slideshow/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.SlideshowDetailView.as_view(), name='slideshow_slide_detail'),

    # default - intro
    url(r'^slideshow/(?P<slug>\S+)/$', 
        views.IntroSlideshowDetailView.as_view(), name='slideshow_detail'),

    # zero version of full intro
    # because when we go back to intro, it's via ajax
    url(r'^full/slideshow/(?P<slug>\S+)/(?P<slide_num_arg>[0])/$', 
        views.ReIntroFullSlideshowDetailView.as_view(), name='full_slideshow_re_intro_detail'),

    #  full screen with slide number
    url(r'^full/slideshow/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.FullSlideshowDetailView.as_view(), name='full_slideshow_slide_detail'),

    # full screen default - intro
    url(r'^full/slideshow/(?P<slug>\S+)/$', 
        views.IntroFullSlideshowDetailView.as_view(), name='intro_full_slideshow_detail'),

    # the moment when you come from a see also on a person full slim
    # re-use ReIntroFullSlideshowDetailView
    url(r'^swapfull/slideshow/(?P<slug>\S+)/$', 
        views.ReIntroFullSlideshowDetailView.as_view(), name='swapfull_slideshow_detail'),


    #  ------ SOCIETY ---
    # choice for vote
    url(r'^society/choice/(?P<slug>\S+)/(?P<slide_num>\d+)/(?P<choice>[0-2])/$', 
        views.SocietyChoiceDetailView.as_view(), name='society_choice'),

    # zero version of intro
    url(r'^society/(?P<slug>\S+)/(?P<slide_num>[0])/$', 
        views.IntroSocietyDetailView.as_view(), name='society_detail'),

    #  with slide number
    url(r'^society/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.SocietyDetailView.as_view(), name='society_slide_detail'),

    # default - intro
    url(r'^society/(?P<slug>\S+)/$', 
        views.IntroSocietyDetailView.as_view(), name='society_detail'),


    # zero version of full intro
    # because when we go back to intro, it's via ajax
    url(r'^full/society/(?P<slug>\S+)/(?P<slide_num_arg>[0])/$', 
        views.ReIntroFullSocietyDetailView.as_view(), name='full_society_re_intro_detail'),

    #  full screen with slide number
    url(r'^full/society/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.FullSocietyDetailView.as_view(), name='full_society_slide_detail'),

    # full screen default - intro
    url(r'^full/society/(?P<slug>\S+)/$', 
        views.IntroFullSocietyDetailView.as_view(), name='full_society_detail'),

    # re-use ReIntroFullSocietyDetailView
    url(r'^swapfull/society/(?P<slug>\S+)/$', 
        views.ReIntroFullSocietyDetailView.as_view(), name='swapfull_society_detail'),



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

    # zero version of full intro
    # because when we go back to intro, it's via ajax
    url(r'^full/footprint/(?P<slug>\S+)/(?P<slide_num_arg>[0])/$', 
        views.ReIntroFullFootprintDetailView.as_view(), name='full_footprint_re_intro_detail'),


    #  full screen with slide number
    url(r'^full/footprint/(?P<slug>\S+)/(?P<slide_num>\d+)/$', 
        views.FullFootprintDetailView.as_view(), name='full_footprint_slide_detail'),

    # full screen default - intro
    url(r'^full/footprint/(?P<slug>\S+)/$', 
        views.IntroFullFootprintDetailView.as_view(), name='full_footprint_detail'),

    # re-use ReIntroFullFootprinDetailView
    url(r'^swapfull/footprint/(?P<slug>\S+)/$', 
        views.ReIntroFullFootprintDetailView.as_view(), name='swapfull_footprint_detail'),


    #  ------ TEAM ---
    url(r'^team/feature/$', views.TeamFeatureListView.as_view(), \
        name='team_special_list'),

]
