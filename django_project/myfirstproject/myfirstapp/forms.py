# myfirstapp/forms.py
from django import forms
from .models import Product, ProductFamily

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'family']

class ProductFamilyForm(forms.ModelForm):
    class Meta:
        model = ProductFamily
        fields = ['name']
