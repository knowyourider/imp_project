from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Feature, Frame
from core.views import MobileFullMixin


class FeatureListView(ListView):
    model = Feature
    # print("--- settings.STATUS_LEVEL: " + str(settings.STATUS_LEVEL))
    # Menu doesn't look a this CBV list -- model has separate list for each type
    # queryset = Feature.objects.filter(is_on_menu=True) 
    # , is_on_menu=True status_num__gte=settings.STATUS_LEVEL
    # context_object_name = 'object_list'
    # template_name = 'special/feature_list.html' 

class TeamFeatureListView(FeatureListView):
    template_name = 'supporting/team_item_list.html' 

class FeatureDetailView(MobileFullMixin, DetailView):
    """
    To be sub classed for each special view
    """
    model = Feature

class SlideFeatureDetailView(FeatureDetailView):
    """
    The model for "slides" is called Frame (for legacy reasons)
    """
    # template_name = determined by sub class
    # extend_base - default from MobileFullMixin, or override in sub class
    # link_name and link_class established in  FeatureDetailView  - MobileFullMixin,
    
    # get extend_base into context 
    def get_context_data(self, **kwargs):
        context = super(SlideFeatureDetailView, self).get_context_data(**kwargs)
        # get the feature object
        feature_object = super(SlideFeatureDetailView, self).get_object()

        # return an error message if no slides have been entered in admin
        if feature_object.frame_set.all():
            # use slide_num from param, if it's there
            if 'slide_num' in self.kwargs:
                slide_num_arg = self.kwargs['slide_num']
                # print(" --- slide num in kwargs: " + str(slide_num_arg))
            else: # otherwise, this is zero - the intro
                slide_num_arg = 0
                # print(" --- slide num zeero: " + str(slide_num_arg))

            # get the frame (slide) object
            slide = get_object_or_404(Frame, feature_id=feature_object.id, 
                slide_num=slide_num_arg)
            error_msg = None
        else:
            slide = None
            error_msg = "Error: For feature at least one slide has to be " + \
                "defined in Admin."


        # add variables to context
        context.update({'slide': slide, 'error_msg': error_msg,
        'link_name': self.link_name, 'link_class': self.link_class})
        return context

# ----------- NON-SLIDE FEATURES ---------

# ---- VIDEO ---
class VideoDetailView(FeatureDetailView):
    template_name = "special/video.html"
    
class FullVideoDetailView(VideoDetailView):
    extend_base = 'supporting/base_detail_full.html'
 
class SwapFullVideoDetailView(VideoDetailView):
    extend_base = 'supporting/base_detail_ajax.html'
 

# ---- VOICES ---
class VoiceDetailView(FeatureDetailView):
    template_name = "special/voices.html"
    
class FullVoiceDetailView(VoiceDetailView):
    extend_base = 'supporting/base_detail_full.html'
 
class SwapFullVoiceDetailView(VoiceDetailView):
    extend_base = 'supporting/base_detail_ajax.html'
 

# ---- EXPLORE ---
#  default
class ExploreDetailView(FeatureDetailView):
    template_name="special/explore.html"

#  full screen 
class FullExploreDetailView(ExploreDetailView):
    extend_base = 'supporting/base_detail_full.html'

class SwapFullExploreDetailView(ExploreDetailView):
    extend_base = 'supporting/base_detail_ajax.html'


# ----------- SLIDE-BASED FEATURES ---------

# ---- DISCOVERERS ---
#  default
class DiscoverersDetailView(FeatureDetailView):
    template_name="special/discoverers-vote.html"

    # get choice and evaluate 
    def get_context_data(self, **kwargs):
        context = super(DiscoverersDetailView, self).get_context_data(**kwargs)
        # print(" -- choice: " + self.kwargs['choice'])
        feature_object = super(DiscoverersDetailView, self).get_object()

        # get choice param and convert to int
        votee_num = int(self.kwargs['slide_num'])
        # get the person (frame, aka slide) object
        votee_object = get_object_or_404(Frame, feature_id=feature_object.id, 
            slide_num=votee_num)

        # record the vote
        if votee_object.num_correct:
            votee_object.num_correct += 1
        else:
            votee_object.num_correct = 1
        votee_object.save()

        # add variables to context
        context.update({'votee_object': votee_object})
        return context


# ---- THEN and NOW ---
#  default
class ThenDetailView(SlideFeatureDetailView):
    template_name="special/then.html"

#  full screen 
class FullThenDetailView(ThenDetailView):
    extend_base = 'supporting/base_detail_full.html'

class SwapFullThenDetailView(FullThenDetailView):
    extend_base = 'supporting/base_detail_ajax.html'


# ---- LOOKING ---
#  default
class LookingDetailView(SlideFeatureDetailView):
    template_name="special/looking.html"

#  full screen 
class FullLookingDetailView(LookingDetailView):
    extend_base = 'supporting/base_detail_full.html'

class SwapFullLookingDetailView(FullLookingDetailView):
    extend_base = 'supporting/base_detail_ajax.html'


# ---- SLIDESHOW ---
#  with slide number
class SlideshowDetailView(SlideFeatureDetailView):
    template_name="special/slideshow.html"
    link_name = "slideshow_slide_detail"
    # link_class = "swap_pop" -- default

# default - intro
class IntroSlideshowDetailView(SlideshowDetailView):
    template_name="special/slideshow_intro.html"

#  full screen with slide number - not first slide, so use ajax non-shell 
class FullSlideshowDetailView(SlideFeatureDetailView):
    template_name="special/slideshow.html"
    extend_base = 'supporting/base_detail_ajax.html'
    link_name = 'full_slideshow_slide_detail'
    link_class = 'swap_fullpop'

# full screen default - intro  
class IntroFullSlideshowDetailView(FullSlideshowDetailView):
    template_name="special/slideshow_intro.html"
    extend_base = 'supporting/base_detail_full.html'
    
# full screen - intro  upon ajax return
# need to suppress shell with base_detail_ajax
class ReIntroFullSlideshowDetailView(FullSlideshowDetailView):
    template_name="special/slideshow_intro.html"
    extend_base = 'supporting/base_detail_ajax.html'
    
    
# ---- SOCIETY ---
#  with slide number
class SocietyDetailView(SlideFeatureDetailView):
    template_name="special/society.html"
    link_name = "society_slide_detail"
    # need special swap to re-enable event listener
    link_class = 'quiz_swap'

# default - intro
class IntroSocietyDetailView(SocietyDetailView):
    template_name="special/society_intro.html"
    # regular swap_pop from intro
    link_class = 'swap_pop'


#  full screen with slide number
class FullSocietyDetailView(SocietyDetailView):
    template_name="special/society.html"
    # template_name="special/slim_content_includes/_society.html"
    # extend_base = 'supporting/base_detail_full.html'
    extend_base = 'supporting/base_detail_ajax.html'
    link_name = 'full_society_slide_detail'
    link_class = 'swap_fullpop'

# full screen default - intro  
class IntroFullSocietyDetailView(FullSocietyDetailView):
    template_name="special/society_intro.html"
    extend_base = 'supporting/base_detail_full.html'

# full screen - intro  upon ajax return
class ReIntroFullSocietyDetailView(FullSocietyDetailView):
    template_name="special/society_intro.html"
    extend_base = 'supporting/base_detail_ajax.html'


# choice integer with slide number
class SocietyChoiceDetailView(SlideFeatureDetailView):
    template_name="special/society_choice.html"

    # get choice and evaluate 
    def get_context_data(self, **kwargs):
        context = super(SocietyChoiceDetailView, self).get_context_data(**kwargs)

        # get the ladies answer
        ladies_choice = context["slide"].num_correct

        # print(" -- num_correct: " + str(ladies_choice))
        # print(" -- choice: " + self.kwargs['choice'])

        # get choice param and convert to int
        choice_int = int(self.kwargs['choice'])

        feedback = "<p>"
        # logic
        if choice_int == 1:
            feedback  += "You voted 'affirmative.'  "
            if ladies_choice == 1:
                feedback  +=  "The young ladies also voted in the affirmative!"
            elif ladies_choice == 0:
                feedback  +=  "Sorry,the young ladies voted in the negative."
            elif ladies_choice == 2:
                feedback  +=  "Actually, this is the last topic the young ladies considered \
                and they never recorded their answer!"
            else:
                feedback  +=  "['num_correct' must be set to 1 or 0 in admin for this slide]"

        elif choice_int == 0:
            feedback  += "You voted 'negative.' "
            if ladies_choice == 1:
                feedback  +=  "Sorry,the young ladies voted in the affirmative."
            elif ladies_choice == 0:
                feedback  +=  "The young ladies also voted in the negative!"
            elif ladies_choice == 2:
                feedback  +=  "Actually, this is the last topic the young ladies considered \
                and they never recorded their answer!"
            else:
                feedback  +=  "['num_correct' must be set to 1 or 0 in admin for this slide]"
        else: # just in case
            feedback = "vote didn't come through"
            # print(" --- slide num zeero: " + str(slide_num_arg))
        feedback += "</p>"
        # add variables to context
        context.update({'feedback': feedback})
        return context


# ---- FOOTPRINTS ---
#  with slide number
class FootprintDetailView(SlideFeatureDetailView):
    template_name="special/footprint.html"
    link_name = "footprint_slide_detail"
    # link_class = "swap_pop" -- default

# default - intro
class IntroFootprintDetailView(FootprintDetailView):
    template_name="special/footprint_intro.html"


#  full screen with slide number
class FullFootprintDetailView(SlideFeatureDetailView):
    template_name="special/footprint.html"
    # template_name="special/slim_content_includes/_footprint.html"
    # extend_base = 'supporting/base_detail_full.html'
    extend_base = 'supporting/base_detail_ajax.html'
    link_name = 'full_footprint_slide_detail'
    link_class = 'swap_fullpop'

# full screen default - intro  
class IntroFullFootprintDetailView(FullFootprintDetailView):
    template_name="special/footprint_intro.html"
    extend_base = 'supporting/base_detail_full.html'


# full screen - intro  upon ajax return
class ReIntroFullFootprintDetailView(FullFootprintDetailView):
    template_name="special/footprint_intro.html"
    # template_name="special/slim_content_includes/_footprint_intro.html"
    extend_base = 'supporting/base_detail_ajax.html'

# --- exception - for footprint ----   
def special_footprint(request, image_name):

    template_name = "special/footprint_includes/_" + image_name + ".html"
    return render(request, template_name, {'dummy': 'dummy'})
 










