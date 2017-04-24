from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.core.files.storage import default_storage
from django.conf import settings
from django.views.generic.edit import FormMixin
from django.db.models import Q
from .models import Context, EvidenceItem, FastFact, Person, Page
from .forms import EvidenceItemSearchForm, ContextSearchForm

class ContextListView(FormMixin, ListView):
    """
    Search in the Context case is more complicated than the Context case. 
    We're searching a many to many relationship
    """
    # model = Context
    queryset = Context.objects.filter(status_num__gte=1)
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
            # topics are many to many
            if len(topic_list) > 0 : # < len(self.init_data['gls'])
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                qquery = Q(topics__slug=topic_list[0])

                for topic_choice in topic_list[1:]:
                    qquery.add((Q(topics__slug=topic_choice)), 'OR' ) # , qquery.connector

                self.object_list = self.object_list.filter(qquery)

        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)

class ContextDetailView(DetailView):
    model = Context
    # context_object_name = 'object'
    # template_name = 'supporting/person_detail.html'


class EvidenceItemListView(FormMixin, ListView):
    """
    The EvidenceItem case is simpler than the Context case. "evidence_type" 
    is directly a field of Evidence item. (Context has many to many associations)
    """
    # model = EvidenceItem
    queryset = EvidenceItem.objects.filter(status_num__gte=1)
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


class EvidenceItemDetailView(DetailView):
    """
    Used with pk for team lists
    """
    model = EvidenceItem
    # context_object_name = 'object'
    # template_name = 'supporting/evidenceitem_detail.html'


class ArtifactDetailView(EvidenceItemDetailView):
    # context_object_name = 'object'
    template_name = 'supporting/evidence_detail/artifact.html'


class DocumentDetailView(EvidenceItemDetailView):
    """
    will also be subclassed by artifact page
    """
    template_name = "supporting/evidence_detail/document.html"
    # extend_base - default from FeatureDetailView, or override in sub class
    # links here are borrowed from Special - might use for full version
    link_name = "must-be-overridden-by-subclass-if-needed"
    # link_class overridden by subclass with "noclass" if fullscreen
    link_class = "swap_pop"
    
    # get extend_base into context 
    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        # get the feature object
        evidenceitem_object = super(DocumentDetailView, self).get_object()

        # check to see that slides have been entered in admin
        if evidenceitem_object.page_set.all():
            error_msg = None
            # double check that suffix param is sent
            if 'page_suffix' in self.kwargs:
                page_suffix = self.kwargs['page_suffix']
                # page suffix sent, use it to get page object
                page = get_object_or_404(Page, evidenceitem_id=evidenceitem_object.id, 
                    page_suffix=page_suffix)
            else: # i.e. no param sent, use the first page.    
                pages = Page.objects.filter(evidenceitem_id=evidenceitem_object.id)
                page = pages[0]
        else: # return an error message if no slides have been entered in admin
            page = None
            error_msg = "Error: For feature at least one page has to be " + \
                "defined in Admin."
        # add variables to context
        context.update({'page': page, 'error_msg': error_msg,
        'link_name': self.link_name, 'link_class': self.link_class })
        return context


class ArtifactPageDetailView(EvidenceItemDetailView):
    """
    may change
    """
    template_name = "supporting/evidence_detail/artifact.html"
    
    # get extend_base into context 
    def get_context_data(self, **kwargs):
        context = super(ArtifactPageDetailView, self).get_context_data(**kwargs)
        # get the feature object
        evidenceitem_object = super(ArtifactPageDetailView, self).get_object()

        # check to see that slides have been entered in admin
        if evidenceitem_object.page_set.all():
            error_msg = None
            # double check that suffix param is sent
            if 'page_suffix' in self.kwargs:
                page_suffix = self.kwargs['page_suffix']
                # page suffix sent, use it to get page object
                page = get_object_or_404(Page, evidenceitem_id=evidenceitem_object.id, 
                    page_suffix=page_suffix)
            else: #  no param sent, but should be because this is a page view    
                page = None
                error_msg = "Error: For feature at least one slide has to be " + \
                    "defined in Admin."
        else: # return an error message if no slides have been entered in admin
            page = None
            error_msg = "Error: For feature at least one page has to be " + \
                "defined in Admin."
        # add variables to context
        context.update({'page': page, 'error_msg': error_msg })
        return context

def evidenceitem_detail(request, slug, page_suffix='default'):
    return None


class FastFactDetailView(DetailView):
    model = FastFact
    # context_object_name = 'object'
    # template_name = 'supporting/fastfact_detail.html'


class PersonListView(ListView):
    #model = Person
    queryset = Person.objects.filter(status_num__gte=1)
    # context_object_name = 'object_list'
    # template_name = 'supporting/person_list.html' 

class PersonDetailView(DetailView):
    model = Person
    # context_object_name = 'object'
    # template_name = 'supporting/person_detail.html'



class TeamTemplateView(TemplateView):
    template_name = 'supporting/team_type_list.html' 

