from django import forms
from .models import Counties
from django.forms import ModelChoiceField

#COUNTY =( 
#    ("Arlington", "Arlington"), 
#    ("District of Columbia", "District of Columbia"), 
#    ("Fairfax", "Fairfax"), 
#    ("Montgomery", "Montgomery"),
#)

def get_counties():
  counties = ()
  for county in Counties.objects.using('data').all():
    counties = counties + ((county.county, county.county),)
  return counties
class FilterByCountyForm(forms.Form):
  #county = forms.ModelChoiceField(queryset=Counties.objects.using('data').values_list('county'))
  county = forms.ChoiceField(choices = get_counties())  