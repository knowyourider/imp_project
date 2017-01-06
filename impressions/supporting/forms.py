from django import forms
from .models import EvidenceItem, EvidenceType
# for organization triming
# from django.db import connection
# import itertools

class EvidenceItemSearchForm(forms.Form):
    """
    Patterened after sitewide SearchForms and Lesson search in Mystic
    choices defined by the Python values_list function
    """
    q = forms.CharField(max_length=100, required=False)

    page = forms.IntegerField(required=False)

    # get evidence type list directly from the database
    etypes = forms.MultipleChoiceField(
        choices = EvidenceType.objects.all().values_list('slug', 
            'title').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

    """
    # get tag list directly from the database
    tags = forms.MultipleChoiceField(
        choices = Tag.objects.all().values_list('slug', 
            'title').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

    # get organization list directly from the database
    orgs = forms.MultipleChoiceField(
        choices = Organization.objects.all().values_list('slug', 
            'name').order_by('id'),
        widget  = forms.CheckboxSelectMultiple,
        required=False,
    )

    # each time the form is loaded have init populate organizations
    # with just the organizations that are associated with actions
    def __init__(self, *args, **kwargs):
        super(ActionSearchForm, self).__init__(*args, **kwargs)

        # Going to use raw SQL to get directly at the plan_action_organizations table
        cursor = connection.cursor()
        # Get all the organization ids in that table
        cursor.execute("SELECT organization_id FROM plan_action_organizations")
        # return is in the form of tuples
        org_id_tuples = cursor.fetchall()
        # convert to flat list of integers and use set() to remove duplicates
        org_ids = (list(set(itertools.chain(*org_id_tuples))))

        # print("--- ids: " + str(org_ids))

        self.fields['orgs'].choices = Organization.objects.filter(pk__in=org_ids).\
            values_list('slug', 'name').order_by('name')

        # self.fields['orgs'].choices = Organization.objects.filter(pk__in=[1,4,5]).\
        #     values_list('slug', 'name').order_by('name')

    """
