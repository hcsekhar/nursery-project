# forms.py
from django import forms

class ProductFilterForm(forms.Form):
    category = forms.CharField(required=False)
    subcategory = forms.CharField(required=False)
    brand = forms.CharField(required=False)
    price_range = forms.CharField(required=False)
