from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.core.files.storage import default_storage
from django.conf import settings
from django.views.generic.edit import FormMixin
from django.db.models import Q
from .models import Context, EvidenceItem, FastFact, Person, Page
from .forms import EvidenceItemSearchForm, ContextSearchForm
from core.views import MobileFullMixin

class ContextListView(FormMixin, ListView):
    """
    a.k.a Backdrops
    Search in the Context case is more complicated than the Context case. 
    We're searching a many to many relationship
    """
    # model = Context
    queryset = Context.objects.filter(status_num__gte=settings.STATUS_LEVEL)
    # context_object_name = 'object_list'
    # template_name = 'supporting/person_list.html' 
    # paginate_by=21
    form_class = ContextSearchForm
    init_data = {'q': ''}

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(), # won't be using this
            'prefix': self.get_prefix(),  # don't know what this is
            'data': self.request.GET or self.init_data # None  # will add my data here
        }
    
    def get(self, request, *args, **kwargs):
        # get starting query set -- hopefully won't need this
        self.object_list = self.get_queryset()
        # get the form
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            q = form.cleaned_data['q']
            topic_list = form.cleaned_data['topics']
            
            if q:
                self.object_list = self.object_list.filter(Q(title__icontains=q) | 
                    Q(narrative__icontains=q) )

            """
            # This version widens per checkbox (OR)
            # topics are many to many
            if len(topic_list) > 0 : # < len(self.init_data['gls'])
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                qquery = Q(topics__slug=topic_list[0])
                for topic_choice in topic_list[1:]:
                    qquery.add((Q(topics__slug=topic_choice)), 'OR' ) # , qquery.connector

                self.object_list = self.object_list.filter(qquery)
            """

            # topics - these narrow (and)
            # Patterned after MA food tags
            # we don't go the Q route which seems more suited for OR
            if len(topic_list) > 0 : 

                for idx, val in enumerate(topic_list):
                    self.object_list = self.object_list.filter(topics__slug=topic_list[idx])

        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)

class ContextDetailView(MobileFullMixin, DetailView):
    model = Context
    # context_object_name = 'object'
    # template_name = 'supporting/person_detail.html'

class FullContextDetailView(ContextDetailView):
    extend_base = 'supporting/base_detail_full.html'
    link_name = 'swapfull_'
    link_class = 'swap_fullpop'

class SwapFullContextDetailView(FullContextDetailView):
    extend_base = 'supporting/base_detail_ajax.html'


class EvidenceItemListView(FormMixin, ListView):
    """
    The EvidenceItem case is simpler than the Context case. "evidence_type" 
    is directly a field of Evidence item. (Context has many to many associations)
    """
    # model = EvidenceItem
    queryset = EvidenceItem.objects.filter(status_num__gte=settings.STATUS_LEVEL)
    # context_object_name = 'object_list'
    # template_name = 'supporting/evidenceitem_list.html' 
    # paginate_by=21 -- supplied by url conf
    form_class = EvidenceItemSearchForm
    init_data = {'q': ''}

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(), # won't be using this
            'prefix': self.get_prefix(),  # don't know what this is
            'data': self.request.GET or self.init_data # will add my data here
        }
    
    def get(self, request, *args, **kwargs):
        # get starting query set -- hopefully won't need this
        self.object_list = self.get_queryset()
        # get the form
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            q = form.cleaned_data['q']
            etype_list = form.cleaned_data['etypes']
            if q:
                self.object_list = self.object_list.filter(Q(title__icontains=q) | 
                    Q(narrative__icontains=q) )
            # Item type
            if len(etype_list) > 0 : # < len(self.init_data['gls'])
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                qquery = Q(evidence_type__slug=etype_list[0])

                for etype_choice in etype_list[1:]:
                    qquery.add((Q(evidence_type__slug=etype_choice)), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)

        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)


class EvidenceItemDetailView(MobileFullMixin, DetailView):
    """
    Used with pk for team lists
    """
    model = EvidenceItem
    # context_object_name = 'object'
    # template_name = 'supporting/evidenceitem_detail.html'


class ArtifactDetailView(EvidenceItemDetailView):
    # context_object_name = 'object'
    template_name = 'supporting/evidenceitem_detail.html'


class DocumentDetailView(EvidenceItemDetailView):
    """
    has to get first page
    """
    template_name = "supporting/evidenceitem_detail.html"
    # extend_base - default from FeatureDetailView, or override in sub class
    
    # when we do "fullscreen" we'll need to get extend_base into context 
    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        # get the feature object
        evidenceitem_object = super(DocumentDetailView, self).get_object()

        # check to see that slides have been entered in admin
        if evidenceitem_object.page_set.all():
            error_msg = None
            pages = Page.objects.filter(evidenceitem_id=evidenceitem_object.id)
            page = pages[0]
        else: # return an error message if no slides have been entered in admin
            page = None
            error_msg = "Error: For feature at least one page has to be " + \
                "defined in Admin."
        # add variables to context
        context.update({'page': page, 'error_msg': error_msg })
        return context


class FullDocumentDetailView(DocumentDetailView):
    extend_base = 'supporting/base_detail_full.html'
    link_name = 'swapfull_'
    link_class = 'swap_fullpop'

class SwapFullDocumentDetailView(FullDocumentDetailView):
    extend_base = 'supporting/base_detail_ajax.html'

class FullArtifactDetailView(ArtifactDetailView):
    extend_base = 'supporting/base_detail_full.html'
    link_name = 'swapfull_'
    link_class = 'swap_fullpop'

class SwapFullArtifactDetailView(FullArtifactDetailView):
    extend_base = 'supporting/base_detail_ajax.html'

def evidence_page(request, slug, page_suffix):
    """
    Supports Ajax call to replace current page
    filename param not used here. It's in the url for use by JS 
    that switches the zoomify image. By putting all the info in one url
    I don't need to split it in JS. And the url will work as a non-js fallback.
    """
    d = get_object_or_404(EvidenceItem, slug=slug)

    # get page record for this suffix
    curr_page = d.page_set.get(page_suffix=page_suffix)            

    return render(request, 'supporting/_page_transcription.html', {'object': d, 
        'curr_page': curr_page})


# temp place holder
def evidenceitem_detail(request, slug, page_suffix='default'):
    return None


class FastFactDetailView(MobileFullMixin, DetailView):
    model = FastFact
    # context_object_name = 'object'
    # template_name = 'supporting/fastfact_detail.html'

class FullFastFactDetailView(FastFactDetailView):
    extend_base = 'supporting/base_detail_full.html'


class PersonListView(ListView):
    #model = Person
    queryset = Person.objects.filter(status_num__gte=settings.STATUS_LEVEL)
    # context_object_name = 'object_list'
    # template_name = 'supporting/person_list.html' 

class PersonDetailView(MobileFullMixin, DetailView):
    model = Person
    # context_object_name = 'object'
    # template_name = 'supporting/person_detail.html'
    link_name = "" # empty for no prefix, just e.g. person_detail

class FullPersonDetailView(PersonDetailView):
    extend_base = 'supporting/base_detail_full.html'
    link_name = 'swapfull_'
    link_class = 'swap_fullpop'

class SwapFullPersonDetailView(FullPersonDetailView):
    extend_base = 'supporting/base_detail_ajax.html'

class TeamTemplateView(TemplateView):
    template_name = 'supporting/team_type_list.html' 

