from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.conf import settings
from supporting.models import Person, Context, EvidenceItem
from special.models import Feature
from stories.models import Story
from themes.models import Theme

class HomeTemplateView(TemplateView):
    # template_name = 'index.html' 

    # Temporarily handle comming soon vs. regular home page
    if settings.SITE_ID == 2:
        template_name = 'index-coming.html' 
    else:
        # regular home page
        template_name = 'index.html' 

class IntroTemplateView(TemplateView):
    template_name = 'intro.html' 

# a place-holder -- not triggered by js because there is no "mobile menu"
# to be visible or not. But could be found by google.
class FullIntroTemplateView(TemplateView):
    template_name = 'intro_full.html' 

class TeamHomeTemplateView(TemplateView):
    template_name = 'team_index.html' 


class MobileFullMixin(DetailView):
    """
    To be mixed into each special and supporting view
    Establishes which shell should be extended
    """
    # Default is for slim pop. Sub classes will override for fullscreen or empty
    # dummy for multi-slice specials (foot, slide, society)
    extend_base = 'supporting/base_detail.html'
    # swap pop in regular swap_fullpop for full mobile
    link_class = "swap_pop"
    link_name = "" #must-be-overridden-by-subclass-if-needed
    
    # get extend_base and referrer into context 
    def get_context_data(self, **kwargs):
        context = super(MobileFullMixin, self).get_context_data(**kwargs)

        # determine whether this is from a (internal?) link with a referer
        # Splitting is based on online dinotracksdiscovery.org -- doesn't work with local 127
        # if (self.request.META['HTTP_REFERER']):
        try:
            # record referring path for full-screen back link
            split_path = self.request.META['HTTP_REFERER'].split("/")

            # determin whether ref is from within dinotracks
            # e.g http://dinotracksdiscovery.org/sitemap/
            base_url = split_path[2] 
            # e.g. dinotracksdiscovery.org , (http://127.0.0.1:8000 won't work)

            # print(" ---- split_path[2]: " + split_path[2])
            # print(" -- domain: " + base_url.split(".")[-2])

            if (base_url.split(".")[-2] == "dinotracksdiscovery" ):
            # if (base_url.split(".")[-2] == "0" ):
                # within site
                # e.g http://dinotracksdiscovery.org/sitemap/
                # key:   0/1/   2                   /   3   /  
                referring_path = "/".join(["", split_path[3], ""]) # , ""
                # print(" --- referrer: " + self.request.META['HTTP_REFERER'])
                # print(" --- split_path length: " + str(len(split_path)))
                # print(" -- split_path[5]: " + split_path[5])

                if len(split_path) > 5:
                    # e.g http://dinotracksdiscovery.org/stories/refinement/
                    # key:   0/1/   2                   /   3   /       4  /
                    # space after last / counts (also we're in non-index mode of  
                    # counting re: length)
                    referring_path += split_path[4] + "/"

                    if len(split_path) > 6:
                        # e.g http://dinotracksdiscovery.org/stories/refinement/7/
                        # key:   0/1/   2                   /   3   /       4  /5/
                        # "/".join([split_path[5], ""])
                        referring_path += split_path[5] + "/"
                        # not sure if we ever get here, but just in case
                        if len(split_path) > 7:
                            referring_path += split_path[6] + "/"
            else:
                # refed from external site
                # referring_path = "https://dinotracksdiscovery.org"
                referring_path = "external_ref"

        except KeyError: # in the case of no referrer
            # referring_path = "https://dinotracksdiscovery.org"
            referring_path = "external_ref"
        except IndexError:
            # max index may be 2 
            # e.g http://dinotracksdiscovery.org/ (home)
            # referring_path = "https://dinotracksdiscovery.org"
            referring_path = "external_ref"

        # print(" --- referring_path: " + referring_path)

        context.update({'extend_base': self.extend_base, 
            'referring_path': referring_path, 'link_class': self.link_class,
            'link_name': self.link_name})
        return context    

class SitemapTemplateView(TemplateView):
    template_name = 'sitemap.xml' 

    def get_context_data(self, **kwargs):
        context = super(SitemapTemplateView, self).get_context_data(**kwargs)
        # get the short name
        # print(" -- **kwargs: " + kwargs['slug'])
        page = "impressions"
        # page = kwargs['slug']

        context['stories'] = \
            Story.objects.filter(status_num__gte=settings.STATUS_LEVEL)
        context['themes'] = \
            Theme.objects.filter(status_num__gte=settings.STATUS_LEVEL)
        # get supporting people list
        context['prime_peeps'] = Person.objects.filter(person_level=2)
        context['second_peeps'] = Person.objects.filter(person_level=1)
        context['minor_peeps'] = Person.objects.filter(person_level=0, 
            status_num__gte=settings.STATUS_LEVEL)
        # remaining supporting
        context['backdrops'] = \
            Context.objects.filter(status_num__gte=settings.STATUS_LEVEL)
        context['evidenceitems'] = \
            EvidenceItem.objects.filter(status_num__gte=settings.STATUS_LEVEL)
        context['features'] = \
            Feature.objects.filter(status_num__gte=settings.STATUS_LEVEL)


        # add variables to context
        #context.update({'prime_peps': prime_peps, 'page': page  })
        return context
