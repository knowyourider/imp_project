from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Context, EvidenceItem, FastFact, Person, Special

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

def special_detail(request, slug):
    object = get_object_or_404(Special, slug=slug)
    # if object.special_type == "interactive"
    # Currently "interactive" is find-footprints.
    # In future we could sub-type and say interactive_find-footprints.html
    template_name = "supporting/special_detail/" + object.special_type + ".html"
    return render(request, template_name, {'object': object})

# class SpecialDetailView(DetailView):
#     model = Special
#     # context_object_name = 'object'
#     # template_name = 'supporting/special_detail.html'

def special_footprint(request, image_name):

    template_name = "supporting/special_detail/interactive_includes/_" + image_name + ".html"
    return render(request, template_name, {'dummy': 'dummy'})


