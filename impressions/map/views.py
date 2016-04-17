from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Layer, Site
#from core.views import SiteListMixin

class SiteListMixin(object):
    """
    Retrieve the site locations.
    """
    # Get params
    def get_context_data(self, **kwargs):
         # Call the base implementation first to get a context
        context = super(SiteListMixin, self).get_context_data(**kwargs)
        # get short_name from URLconf
        # short_name = self.kwargs['short_name']

        # first just get list of all sites
        # look for non CBV list in mse
        site_list = Site.objects.all()
        # later get list just for given layer
        # site_list = Site.objects.filter(map_type='Voyage', status_num__gte=settings.STATUS_LEVEL, 
        #	sites__id__exact=settings.SITE_ID).order_by('ordinal')
        # figure how to get parameter for chosen layer


        # get object 
        #resource_object = get_object_or_404(ItemModel, short_name=short_name)
        #context['resource_object'] = resource_object
        context['site_list'] = site_list

        return context


class MapListView(SiteListMixin, ListView):
    model = Layer
    # context_object_name = 'object_list'
    template_name = 'map/map.html' 
