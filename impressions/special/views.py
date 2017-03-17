from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Feature, Frame


class FeatureListView(ListView):
    #model = Feature
    queryset = Feature.objects.filter(status_num__gte=1, is_on_menu=True)
    # context_object_name = 'object_list'
    # template_name = 'special/feature_list.html' 

class TeamFeatureListView(FeatureListView):
    template_name = 'supporting/team_item_list.html' 

class FeatureDetailView(DetailView):
    """
    To be sub classed for each special view
    """
    model = Feature
    # context_object_name = 'object'
    # template_name = feature_detail.html - there's a placeholder for this
    # Default is for slim pop. Sub classe will override for fullscreen
    extend_base = 'supporting/base_detail.html'
    
    # get extend_base into context 
    def get_context_data(self, **kwargs):
        context = super(FeatureDetailView, self).get_context_data(**kwargs)
        context.update({'extend_base': self.extend_base})
        return context    


class SlideFeatureDetailView(FeatureDetailView):
    """
    The model for "slides" is called Frame (for legacy reasons)
    """
    # template_name = determined by sub class
    # extend_base - default from FeatureDetailView, or override in sub class
    link_name = "must-be-overridden-by-subclass-if-needed"
    # link_class overridden by subclass with "noclass" if fullscreen
    link_class = "swap_pop"
    
    # get extend_base into context 
    def get_context_data(self, **kwargs):
        context = super(SlideFeatureDetailView, self).get_context_data(**kwargs)
        # get the feature object
        feature_object = super(SlideFeatureDetailView, self).get_object()

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

        # add variables to context
        context.update({'slide': slide,
        'link_name': self.link_name, 'link_class': self.link_class })
        return context

# ----------- NON-SLIDE FEATURES ---------

# ---- VIDEO ---
class VideoDetailView(FeatureDetailView):
    template_name = "special/video.html"
    
class FullVideoDetailView(VideoDetailView):
    extend_base = 'supporting/base_detail_full.html'
 

# ---- VOICES ---
class VoiceDetailView(FeatureDetailView):
    template_name = "special/voices.html"
    
class FullVoiceDetailView(VoiceDetailView):
    extend_base = 'supporting/base_detail_full.html'
 

# ---- EXPLORE ---
#  default
class ExploreDetailView(FeatureDetailView):
    template_name="special/explore.html"

#  full screen 
class FullExploreDetailView(ExploreDetailView):
    extend_base = 'supporting/base_detail_full.html'


# ----------- SLIDE-BASED FEATURES ---------

# ---- DISCOVERERS ---
#  default
class DiscoverersDetailView(SlideFeatureDetailView):
    template_name="special/discoverers.html"

# ---- THEN and NOW ---
#  default
class ThenDetailView(SlideFeatureDetailView):
    template_name="special/then.html"

#  full screen 
class FullThenDetailView(ThenDetailView):
    extend_base = 'supporting/base_detail_full.html'


# ---- LOOKING ---
#  default
class LookingDetailView(SlideFeatureDetailView):
    template_name="special/looking.html"

#  full screen 
class FullLookingDetailView(LookingDetailView):
    extend_base = 'supporting/base_detail_full.html'


# ---- SLIDESHOW ---
#  with slide number
class SlideshowDetailView(SlideFeatureDetailView):
    template_name="special/slideshow.html"
    link_name = "slideshow_slide_detail"
    # link_class = "swap_pop" -- default

# default - intro
class IntroSlideshowDetailView(SlideshowDetailView):
    template_name="special/slideshow_intro.html"

#  full screen with slide number
class FullSlideshowDetailView(SlideFeatureDetailView):
    template_name="special/slideshow.html"
    extend_base = 'supporting/base_detail_full.html'
    link_name = 'full_slideshow_slide_detail'
    link_class = 'noclass'

# full screen default - intro  
class IntroFullSlideshowDetailView(FullSlideshowDetailView):
    template_name="special/slideshow_intro.html"
    
    
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
    extend_base = 'supporting/base_detail_full.html'
    link_name = 'full_footprint_slide_detail'
    link_class = 'noclass'

# full screen default - intro  
class IntroFullFootprintDetailView(FullFootprintDetailView):
    template_name="special/footprint_intro.html"

# --- exception - for footprint ----   
def special_footprint(request, image_name):

    template_name = "special/footprint_includes/_" + image_name + ".html"
    return render(request, template_name, {'dummy': 'dummy'})
 

    """
    Lots of "special" cases, so opting for a def.
    Legacy from supporting types, so info about sub-types
    came from the object itself (not from url name)
    The slide_num_arg is optional, so far for interactives and slideshow
    Slide is the legacy model name, but I'm using Frame in order to avoid conflict
    """
"""    
def feature_detail(request, slug, slide_num_arg=0):
    object = get_object_or_404(Feature, slug=slug)
    # each type has its own template
    # template_name = "supporting/special_detail/" + object.special_type + ".html"
    special_type = object.special_type

    # determine whether this is the stand-alone version of the URL
    # If so, set extend_base to 'supporting/base_detail_alone.html'
    # 2nd slice will be either feature or fullfeature
    url_version = request.path_info.split("/")[2]
    extend_base = 'supporting/base_detail.html'
    if (url_version == 'fullfeature'):
        extend_base = 'supporting/base_detail_full.html'
        
    # print("--- extend_base: " + extend_base)

    # interactives and slideshows share the slide structure
    # In both cases re-loding the whole page -- not much that would stay in place if
    # I used AJAX
    if special_type == "footprint" or special_type == "slideshow" or special_type == "then":
        slide = get_object_or_404(Frame, feature_id=object.id, 
            slide_num=slide_num_arg)
        # Currently "interactive" is find-footprints.
        # In future we could sub-type and say interactive_find-footprints.html

        # for interactive and slideshow slide = 0 add intro to special type
        # when slide_num_arg is passed as param it's a string, so convert to be sure
        slide_num_arg = int(slide_num_arg)

        # add intro for interactive and slideshow zero, but not for then and now
        if (slide_num_arg==0 and special_type != "then"):
            special_type += "_intro"

        # add _full for full url version of footprint
        # Maybe _full should go before intro, cover for all special types
        if (url_version == 'fullfeature'):
            special_type += "_full"

        # print("special_type in slideshow: " + special_type)
        print("--- url_version: " + url_version)

        return render(request, "special/" + special_type + ".html", 
            {'object': object, 'slide': slide, 'extend_base': extend_base})
    else:
        # add _full for full url version of jurassic
        # Refactor to avoid duplication
        # if (url_version == 'fullfeature'):
        #     special_type += "_full"

        return render(request, "special/" + special_type + ".html", 
            {'object': object, 'extend_base': extend_base})
        
"""