# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Panier, PanierProduit, Price, Produit, FamilleProduit, PointDeVente
from .forms import (
    PanierForm, PanierProduitForm, PriceForm, ProduitForm, FamilleProduitForm, PointDeVenteForm
)

from django.shortcuts import render

def accueil(request):
    return render(request, 'myfirstapp/accueil.html')


# Vues pour Panier
def panier_list(request):
    paniers = Panier.objects.all()
    return render(request, 'myfirstapp/panier_list.html', {'paniers': paniers})

def panier_detail(request, pk):
    panier = get_object_or_404(Panier, pk=pk)
    return render(request, 'myfirstapp/panier_detail.html', {'panier': panier})

def panier_new(request):
    if request.method == "POST":
        form = PanierForm(request.POST)
        if form.is_valid():
            panier = form.save(commit=False)
            panier.save()
            return redirect('panier_detail', pk=panier.pk)
    else:
        form = PanierForm()
    return render(request, 'myfirstapp/panier_edit.html', {'form': form})

def panier_edit(request, pk):
    panier = get_object_or_404(Panier, pk=pk)
    if request.method == "POST":
        form = PanierForm(request.POST, instance=panier)
        if form.is_valid():
            panier = form.save(commit=False)
            panier.save()
            return redirect('panier_detail', pk=panier.pk)
    else:
        form = PanierForm(instance=panier)
    return render(request, 'myfirstapp/panier_edit.html', {'form': form})

def panier_delete(request, pk):
    panier = get_object_or_404(Panier, pk=pk)
    panier.delete()
    return redirect('panier_list')


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Price, Produit
from .forms import PriceForm, ProduitForm

# Vues pour Price
def price_list(request):
    prices = Price.objects.all()
    return render(request, 'myfirstapp/price_list.html', {'prices': prices})

def price_detail(request, pk):
    price = get_object_or_404(Price, pk=pk)
    return render(request, 'myfirstapp/price_detail.html', {'price': price})

def price_new(request):
    if request.method == "POST":
        form = PriceForm(request.POST)
        if form.is_valid():
            price = form.save(commit=False)
            price.save()
            return redirect('price_detail', pk=price.pk)
    else:
        form = PriceForm()
    return render(request, 'myfirstapp/price_edit.html', {'form': form})

def price_edit(request, pk):
    price = get_object_or_404(Price, pk=pk)
    if request.method == "POST":
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            price = form.save(commit=False)
            price.save()
            return redirect('price_detail', pk=price.pk)
    else:
        form = PriceForm(instance=price)
    return render(request, 'myfirstapp/price_edit.html', {'form': form})

def price_delete(request, pk):
    price = get_object_or_404(Price, pk=pk)
    price.delete()
    return redirect('price_list')

# Vues pour Produit
def produit_list(request):
    produits = Produit.objects.all()
    return render(request, 'myfirstapp/produit_list.html', {'produits': produits})

def produit_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'myfirstapp/produit_detail.html', {'produit': produit})

def produit_new(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save(commit=False)
            produit.save()
            return redirect('produit_detail', pk=produit.pk)
    else:
        form = ProduitForm()
    return render(request, 'myfirstapp/produit_edit.html', {'form': form})

def produit_edit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == "POST":
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            produit = form.save(commit=False)
            produit.save()
            return redirect('produit_detail', pk=produit.pk)
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'myfirstapp/produit_edit.html', {'form': form})

def produit_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    return redirect('produit_list')




# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import FamilleProduit, PointDeVente
from .forms import FamilleProduitForm, PointDeVenteForm

# Vues pour FamilleProduit
def famille_produit_list(request):
    famille_produits = FamilleProduit.objects.all()
    return render(request, 'myfirstapp/famille_produit_list.html', {'famille_produits': famille_produits})

def famille_produit_detail(request, pk):
    famille_produit = get_object_or_404(FamilleProduit, pk=pk)
    return render(request, 'myfirstapp/famille_produit_detail.html', {'famille_produit': famille_produit})

def famille_produit_new(request):
    if request.method == "POST":
        form = FamilleProduitForm(request.POST)
        if form.is_valid():
            famille_produit = form.save(commit=False)
            famille_produit.save()
            return redirect('famille_produit_detail', pk=famille_produit.pk)
    else:
        form = FamilleProduitForm()
    return render(request, 'myfirstapp/famille_produit_edit.html', {'form': form})

def famille_produit_edit(request, pk):
    famille_produit = get_object_or_404(FamilleProduit, pk=pk)
    if request.method == "POST":
        form = FamilleProduitForm(request.POST, instance=famille_produit)
        if form.is_valid():
            famille_produit = form.save(commit=False)
            famille_produit.save()
            return redirect('famille_produit_detail', pk=famille_produit.pk)
    else:
        form = FamilleProduitForm(instance=famille_produit)
    return render(request, 'myfirstapp/famille_produit_edit.html', {'form': form})

def famille_produit_delete(request, pk):
    famille_produit = get_object_or_404(FamilleProduit, pk=pk)
    famille_produit.delete()
    return redirect('famille_produit_list')

# Vues pour PointDeVente
def point_de_vente_list(request):
    points_de_vente = PointDeVente.objects.all()
    return render(request, 'myfirstapp/point_de_vente_list.html', {'points_de_vente': points_de_vente})

def point_de_vente_detail(request, pk):
    point_de_vente = get_object_or_404(PointDeVente, pk=pk)
    return render(request, 'myfirstapp/point_de_vente_detail.html', {'point_de_vente': point_de_vente})

def point_de_vente_new(request):
    if request.method == "POST":
        form = PointDeVenteForm(request.POST)
        if form.is_valid():
            point_de_vente = form.save(commit=False)
            point_de_vente.save()
            return redirect('point_de_vente_detail', pk=point_de_vente.pk)
    else:
        form = PointDeVenteForm()
    return render(request, 'myfirstapp/point_de_vente_edit.html', {'form': form})

def point_de_vente_edit(request, pk):
    point_de_vente = get_object_or_404(PointDeVente, pk=pk)
    if request.method == "POST":
        form = PointDeVenteForm(request.POST, instance=point_de_vente)
        if form.is_valid():
            point_de_vente = form.save(commit=False)
            point_de_vente.save()
            return redirect('point_de_vente_detail', pk=point_de_vente.pk)
    else:
        form = PointDeVenteForm(instance=point_de_vente)
    return render(request, 'myfirstapp/point_de_vente_edit.html', {'form': form})

def point_de_vente_delete(request, pk):
    point_de_vente = get_object_or_404(PointDeVente, pk=pk)
    point_de_vente.delete()
    return redirect('point_de_vente_list')

