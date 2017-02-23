from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Feature, Frame


class FeatureListView(ListView):
    #model = Special
    queryset = Feature.objects.filter(status_num__gte=1)
    # context_object_name = 'object_list'
    # template_name = 'special/feature_list.html' 


def feature_detail(request, slug, slide_num_arg=0):
    """
    Lots of "special" cases, so opting for a def.
    The urls need to stay consistent with other supporting types, so info about sub-types
    has to come from the object itself (not from extra params)
    The slide_num_arg is optional, so far for interactives and slideshow
    """
    object = get_object_or_404(Feature, slug=slug)
    # each type has its own template
    # template_name = "supporting/special_detail/" + object.special_type + ".html"
    special_type = object.special_type

    # determine whether this is the stand-alone version of the URL
    # If so, set extend_base to 'supporting/base_detail_alone.html'
    # 2nd slice will be either special or fullspecial
    url_version = request.path_info.split("/")[2]
    extend_base = 'supporting/base_detail.html'
    if (url_version == 'fullspecial'):
        extend_base = 'supporting/base_detail_alone.html'
        
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

        # add _full for full url version of footpring
        if (url_version == 'fullspecial'):
            special_type += "_full"

        # print("special_type in slideshow: " + special_type)
        print("--- url_version: " + url_version)

        return render(request, "special/" + special_type + ".html", 
            {'object': object, 'slide': slide, 'extend_base': extend_base})
    else:
        return render(request, "special/" + special_type + ".html", 
            {'object': object, 'extend_base': extend_base})
        
def special_footprint(request, image_name):

    template_name = "special/footprint_includes/_" + image_name + ".html"
    return render(request, template_name, {'dummy': 'dummy'})

