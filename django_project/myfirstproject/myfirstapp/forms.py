# forms.py
from django import forms
from .models import PointDeVente, FamilleProduit, Produit, Price, Panier, PanierProduit

class PointDeVenteForm(forms.ModelForm):
    class Meta:
        model = PointDeVente
        fields = ['code', 'wilaya', 'moughataa', 'commune', 'gps_lat', 'gps_long']

class FamilleProduitForm(forms.ModelForm):
    class Meta:
        model = FamilleProduit
        fields = ['label']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['label', 'price_unit', 'code', 'famille_produit']

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['value', 'date', 'point', 'produit']

class PanierForm(forms.ModelForm):
    class Meta:
        model = Panier
        fields = ['label', 'code', 'description']

class PanierProduitForm(forms.ModelForm):
    class Meta:
        model = PanierProduit
        fields = ['price', 'panier', 'ponderation']

