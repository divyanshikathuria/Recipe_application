from django import forms
from recipe.models import Info

class SearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=40)
