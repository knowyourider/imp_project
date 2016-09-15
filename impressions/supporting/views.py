from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Context, EvidenceItem, FastFact, Person, Special, Slide

class ContextListView(ListView):
    # model = Context
    queryset = Context.objects.filter(status_num__gte=2)
    # context_object_name = 'object_list'
    # template_name = 'supporting/person_list.html' 

class ContextDetailView(DetailView):
    model = Context
    # context_object_name = 'object'
    # template_name = 'supporting/person_detail.html'


class EvidenceItemListView(ListView):
    # model = EvidenceItem
    queryset = EvidenceItem.objects.filter(status_num__gte=2)
    # context_object_name = 'object_list'
    # template_name = 'supporting/evidenceitem_list.html' 

class EvidenceItemDetailView(DetailView):
    model = EvidenceItem
    # context_object_name = 'object'
    # template_name = 'supporting/evidenceitem_detail.html'


class FastFactDetailView(DetailView):
    model = FastFact
    # context_object_name = 'object'
    # template_name = 'supporting/fastfact_detail.html'


class PersonListView(ListView):
    #model = Person
    queryset = Person.objects.filter(status_num__gte=2)
    # context_object_name = 'object_list'
    # template_name = 'supporting/person_list.html' 

class PersonDetailView(DetailView):
    model = Person
    # context_object_name = 'object'
    # template_name = 'supporting/person_detail.html'

class SpecialListView(ListView):
    #model = Special
    queryset = Special.objects.filter(status_num__gte=2)
    # context_object_name = 'object_list'
    # template_name = 'supporting/special_list.html' 

def special_detail(request, slug, slide_num_arg=1):
    """
    Lots of "special" cases, so opting for a def.
    The urls need to stay consistent with other supporting types, so info about sub-types
    has to come from the object itself (not from extra params)
    The slide_num_arg is optional, so far for interactives and slideshow
    """
    object = get_object_or_404(Special, slug=slug)
    # each type has its own template
    template_name = "supporting/special_detail/" + object.special_type + ".html"
    # interactives and slideshows share the slide structure
    # In both cases re-loding the whole page -- not much that would stay in place if
    # I used AJAX
    if object.special_type == "interactive" or object.special_type == "slideshow" or object.special_type == "then":
        slide = get_object_or_404(Slide, special_id=object.id, 
            slide_num=slide_num_arg)
        # Currently "interactive" is find-footprints.
        # In future we could sub-type and say interactive_find-footprints.html
        return render(request, template_name, {'object': object, 'slide': slide})
    else:
        return render(request, template_name, {'object': object})
        
def special_footprint(request, image_name):

    template_name = "supporting/special_detail/interactive_includes/_" + image_name + ".html"
    return render(request, template_name, {'dummy': 'dummy'})


