# myfirstapp/resources.py
from import_export import resources
from .models import Panier, FamilleProduit, Price, PanierProduit, Produit 

class PanierResource(resources.ModelResource):
    class Meta:
        model = Panier
        skip_unchanged = True
        report_skipped = False
        fields = ('label', 'code', 'description')


class FamilleProduitResource(resources.ModelResource):
    class Meta:
        model = FamilleProduit
        skip_unchanged = True
        report_skipped = False
        fields = ('label',)


class PriceResource(resources.ModelResource):
    class Meta:
        model = Price
        skip_unchanged = True
        report_skipped = False
        fields = ('value', 'date', 'point_ID', 'produit_ID',)


class PanierProduitResource(resources.ModelResource):
    class Meta:
        model = PanierProduit
        skip_unchanged = True
        report_skipped = False
        fields = ('price_ID__value', 'panier_ID__label', 'ponderation',)



class ProduitResource(resources.ModelResource):
    class Meta:
        model = Produit
        skip_unchanged = True
        report_skipped = False
        fields = ('label', 'price_unit', 'code', 'famille_produit_ID',)