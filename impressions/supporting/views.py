from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.files.storage import default_storage
from django.conf import settings
from .models import Context, EvidenceItem, FastFact, Person, Special, Slide, Page

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

def evidenceitem_detail(request, slug, page_suffix='default'):
    """
    Patterened after special_detail
    Several evidenceitem types, so opting for a def.
    The urls need to stay consistent with other evidence types, so info about sub-types
    has to come from the object itself (not from extra params)
    The page_suffix is optional, so far for documents
    """
    object = get_object_or_404(EvidenceItem, slug=slug)
    # each type has its own template
    # template_name = "supporting/special_detail/" + object.special_type + ".html"
    evidence_type_slug = object.evidence_type.slug

    # print("------  evidence_type_slug: " + evidence_type_slug)

    # zoom_exists needs to be set for all cases, so set default in advance
    _zoom_exists = False

    # ??re-loding the whole (slim) page -- not much that would stay in place if
    # I used AJAX

    # Handle document paging
    if evidence_type_slug == "manuscript" or evidence_type_slug == "print":

        # Documents (Manuscripts or Prin) have to have at least one page set in admin 
        # if there are pages, 
        #   if suffix sent use it,
        #   else use find and use first page
        # else no page
        #   send error message
        # try:  
        if object.page_set.all():
            # print("---- page set exists: ")
            if (page_suffix == 'default'):
                # i.e. no param sent, use the first page.
                pages = Page.objects.filter(evidenceitem_id=object.id)
                page = pages[0]
            else:
                # page suffix sent, use it
                page = get_object_or_404(Page, evidenceitem_id=object.id, 
                    page_suffix=page_suffix)
            error_msg = None
            # See if zoom exists, using suffix
            _zoom_exists = zoom_exists(object.slug + '-' + page.page_suffix)

        else:
            page = None
            error_msg = "Error: For manuscripts and print at least one page has to be defined in Admin."
            # print("----- no page set ")

        # return render(request, "supporting/evidence_detail/" + evidence_type_slug + ".html", 
        return render(request, "supporting/evidence_detail/document.html", 
            {'object': object, 'page': page, 'error_msg': error_msg, 'zoom_exists': _zoom_exists}) 
    else:
        # See if zoom exists, (no suffix)
        _zoom_exists = zoom_exists(object.slug)
        return render(request, "supporting/evidenceitem_detail.html", 
            {'object': object, 'zoom_exists': _zoom_exists})

def zoom_exists(zoom_dir):
    full_filepath = settings.BASE_DIR + '/supporting/static/supporting/evidenceitem/zooms/' + zoom_dir 
    # print("--- zoom_dir: " + zoom_dir)
    # print("--- full_filepath: " + full_filepath)
    if default_storage.exists(full_filepath):
        return True
    else:
        return False

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

def special_detail(request, slug, slide_num_arg=0):
    """
    Lots of "special" cases, so opting for a def.
    The urls need to stay consistent with other supporting types, so info about sub-types
    has to come from the object itself (not from extra params)
    The slide_num_arg is optional, so far for interactives and slideshow
    """
    object = get_object_or_404(Special, slug=slug)
    # each type has its own template
    # template_name = "supporting/special_detail/" + object.special_type + ".html"
    special_type = object.special_type

    # print("special_type: " + special_type)

    # interactives and slideshows share the slide structure
    # In both cases re-loding the whole page -- not much that would stay in place if
    # I used AJAX
    if special_type == "interactive" or special_type == "slideshow" or special_type == "then":
        slide = get_object_or_404(Slide, special_id=object.id, 
            slide_num=slide_num_arg)
        # Currently "interactive" is find-footprints.
        # In future we could sub-type and say interactive_find-footprints.html

        # for interactive and slideshow slide = 0 add intro to special type
        # when slide_num_arg is passed as param it's a string, so convert to be sure
        slide_num_arg = int(slide_num_arg)
        # add intro for interactive and slideshow, but not for then and now
        if (slide_num_arg==0 and special_type != "then"):
            special_type += "_intro"

        # print("special_type in slideshow: " + special_type)

        return render(request, "supporting/special_detail/" + special_type + ".html", 
            {'object': object, 'slide': slide})
    else:
        return render(request, "supporting/special_detail/" + special_type + ".html", 
            {'object': object})
        
def special_footprint(request, image_name):

    template_name = "supporting/special_detail/interactive_includes/_" + image_name + ".html"
    return render(request, template_name, {'dummy': 'dummy'})


