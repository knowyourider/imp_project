from django.urls import path, re_path
from . import views

app_name="special"

urlpatterns = [
    path('feature/', views.FeatureListView.as_view(), name='feature_list'),

    # CBV approach
    # The first part of each name has to match the corresponding
    # name in special.Feature.special_type, e.g. "video"_detail
    # Applies only to the "staring" names, not subsequent slide details

    # ----------- NON-SLIDE FEATURES ---------

    #  ------ VIDEO ---
    path('video/<slug:slug>/', 
        views.FullVideoDetailView.as_view(), name='video_detail'),

    path('ajax/video/<slug:slug>/', 
        views.VideoDetailView.as_view(), name='ajax_video_detail'),

    path('swapfull/video/<slug:slug>/', 
        views.SwapFullVideoDetailView.as_view(), name='swapfull_video_detail'),

    #  ------ VOICE ---
    # Should have been voice, singular, but too hard to change now
    path('voices/<slug:slug>/', 
        views.FullVoiceDetailView.as_view(), name='voices_detail'),

    path('ajax/voices/<slug:slug>/', 
        views.VoiceDetailView.as_view(), name='ajax_voices_detail'),

    path('swapfull/voices/<slug:slug>/', 
        views.SwapFullVoiceDetailView.as_view(), name='swapfull_voices_detail'),

    #  ------ EXPLORE ---
    path('explore/<slug:slug>/', 
        views.FullExploreDetailView.as_view(), name='explore_detail'),

    path('ajax/explore/<slug:slug>/', 
        views.ExploreDetailView.as_view(), name='ajax_explore_detail'),

    path('swapfull/explore/<slug:slug>/', 
        views.SwapFullExploreDetailView.as_view(), name='swapfull_explore_detail'),

    #  ------ DICOVERERS ---
    # Not stand-alone -- only serves voting in Whose Discovery, Chapter 8
    path('discoverers/<slug:slug>/<slide_num>/', 
        views.DiscoverersDetailView.as_view(), name='discoverers_detail'),

    # ----------- SLIDE-BASED FEATURES ---------

    #  ------ THEN AND NOW ---
    path('then/<slug:slug>/', 
        views.FullThenDetailView.as_view(), name='then_detail'),

    path('ajax/then/<slug:slug>/', 
        views.ThenDetailView.as_view(), name='ajax_then_detail'),

    path('swapfull/then/<slug:slug>/', 
        views.SwapFullThenDetailView.as_view(), name='swapfull_then_detail'),

    #  ------ LOOKING ---
    path('looking/<slug:slug>/', 
        views.FullLookingDetailView.as_view(), name='looking_detail'),

    path('ajax/looking/<slug:slug>/', 
        views.LookingDetailView.as_view(), name='ajax_looking_detail'),

    path('swapfull/looking/<slug:slug>/', 
        views.SwapFullLookingDetailView.as_view(), name='swapfull_looking_detail'),


    #  ------ SLIDESHOW ---
    # Zero param must also go to intro. We're dependent on the link_name 
    # which distinguishes full from slim pop, so we can't just use 
    # slideshow_detail (no int param) for the link in nav
    re_path('slideshow/<slug:slug>/(?P<slide_num_arg>[0])/', 
        views.IntroSlideshowDetailView.as_view(), name='reintro-slideshow_detail'),

    #  with slide number (other than 0)
    path('slideshow/<slug:slug>/<slide_num>/', 
        views.SlideshowDetailView.as_view(), name='slideshow_slide_detail'),

    # default - full (changed Nov 1, 2017)
    path('slideshow/<slug:slug>/', 
        views.IntroFullSlideshowDetailView.as_view(), name='slideshow_detail'),

    # zero version of full intro
    # because when we go back to intro, it's via ajax
    re_path('full/slideshow/<slug:slug>/(?P<slide_num_arg>[0])/', 
        views.ReIntroFullSlideshowDetailView.as_view(), name='full_slideshow_re_intro_detail'),

    #  full screen with slide number
    path('full/slideshow/<slug:slug>/<slide_num>/', 
        views.FullSlideshowDetailView.as_view(), name='full_slideshow_slide_detail'),

    # ajax screen default - intro (changed Nov 1, 2017)
    path('ajax/slideshow/<slug:slug>/', 
        views.IntroSlideshowDetailView.as_view(), name='intro_ajax_slideshow_detail'),

    # the moment when you come from a see also on a person full slim
    # re-use ReIntroFullSlideshowDetailView
    path('swapfull/slideshow/<slug:slug>/', 
        views.ReIntroFullSlideshowDetailView.as_view(), name='swapfull_slideshow_detail'),


    #  ------ SOCIETY ---
    # choice for vote
    path('society/choice/<slug:slug>/<slide_num>/<int:choice>)/', 
        views.SocietyChoiceDetailView.as_view(), name='society_choice'),

    # zero version of intro
    re_path('society/<slug:slug>/(?P<slide_num>[0])/', 
        views.IntroSocietyDetailView.as_view(), name='society_detail'),

    #  with slide number
    path('society/<slug:slug>/<slide_num>/', 
        views.SocietyDetailView.as_view(), name='society_slide_detail'),

    # default - intro (changed Nov 1, 2017)
    path('society/<slug:slug>/', 
        views.IntroFullSocietyDetailView.as_view(), name='society_detail'),


    # zero version of full intro
    # because when we go back to intro, it's via ajax
    re_path('full/society/<slug:slug>/(?P<slide_num_arg>[0])/', 
        views.ReIntroFullSocietyDetailView.as_view(), name='full_society_re_intro_detail'),

    #  full screen with slide number
    path('full/society/<slug:slug>/<slide_num>/', 
        views.FullSocietyDetailView.as_view(), name='full_society_slide_detail'),

    # ajax screen default - intro (changed Nov 1, 2017)
    path('ajax/society/<slug:slug>/', 
        views.IntroSocietyDetailView.as_view(), name='ajax_society_detail'),

    # re-use ReIntroFullSocietyDetailView
    path('swapfull/society/<slug:slug>/', 
        views.ReIntroFullSocietyDetailView.as_view(), name='swapfull_society_detail'),



    #  ------ FOOTPRINTS ---
    # zero version of intro
    re_path('footprint/<slug:slug>/(?P<slide_num>[0])/', 
        views.IntroFootprintDetailView.as_view(), name='footprint_detail'),

    #  with slide number
    path('footprint/<slug:slug>/<slide_num>/', 
        views.FootprintDetailView.as_view(), name='footprint_slide_detail'),

    # default full - intro (changed Nov 1, 2017)
    path('footprint/<slug:slug>/', 
        views.IntroFullFootprintDetailView.as_view(), name='footprint_detail'),

    # zero version of full intro
    # because when we go back to intro, it's via ajax
    re_path('full/footprint/<slug:slug>/(?P<slide_num_arg>[0])/', 
        views.ReIntroFullFootprintDetailView.as_view(), name='full_footprint_re_intro_detail'),


    #  full screen with slide number
    path('full/footprint/<slug:slug>/<slide_num>/', 
        views.FullFootprintDetailView.as_view(), name='full_footprint_slide_detail'),

    # ajax screen default - intro (changed Nov 1, 2017)
    path('ajax/footprint/<slug:slug>/', 
        views.IntroFootprintDetailView.as_view(), name='ajax_footprint_detail'),

    # re-use ReIntroFullFootprinDetailView
    path('swapfull/footprint/<slug:slug>/', 
        views.ReIntroFullFootprintDetailView.as_view(), name='swapfull_footprint_detail'),


    #  ------ TEAM ---
    path('team/feature/', views.TeamFeatureListView.as_view(), \
        name='team_special_list'),

]
