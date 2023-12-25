# myfirstapp/admin.py
from django.contrib import admin
from .models import Panier, PanierProduit, Price, Produit, FamilleProduit, PointDeVente

admin.site.register(Panier)
admin.site.register(PanierProduit)
admin.site.register(Price)
admin.site.register(Produit)
admin.site.register(FamilleProduit)
admin.site.register(PointDeVente)

