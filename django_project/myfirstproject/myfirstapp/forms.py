# forms.py
from django import forms
from .models import PointDeVente, FamilleProduit, Produit, Price, Panier, PanierProduit

class PointDeVenteForm(forms.ModelForm):
    class Meta:
        model = PointDeVente
        fields = ['code', 'wilaya', 'moughataa', 'commune', 'gps_lat', 'gps_long']
        
        
from django import forms

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
        

class FamilleProduitForm(forms.ModelForm):
    class Meta:
        model = FamilleProduit
        fields = ['label']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['label', 'price_unit', 'code', 'famille_produit_ID']

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['value', 'date', 'point_ID', 'produit_ID']

class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = ['label', 'code', 'description']

from django import forms
from .models import PanierProduit

class PanierProduitForm(forms.ModelForm):
    class Meta:
        model = PanierProduit
        fields = ['price_ID', 'panier_ID', 'ponderation']

from django import forms
from .models import Price

class PriceImportForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['value', 'date', 'point_ID', 'produit_ID']








# myfirstapp/forms.py
from django import forms

class PredictionForm(forms.Form):
    prediction_date = forms.DateField(
        label='Prediction Date',
        widget=forms.SelectDateWidget(years=[2024])  # Only include the year 2024
    )




