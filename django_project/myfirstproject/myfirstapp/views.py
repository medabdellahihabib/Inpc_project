# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Panier, PanierProduit, Price, Produit, FamilleProduit, PointDeVente
from .forms import (
    PanierForm, PanierProduitForm, PriceForm, ProduitForm, FamilleProduitForm, PointDeVenteForm
)

from django.shortcuts import render

def accueil(request):
    return render(request, 'myfirstapp/accueil.html')


def services(request):
    return render(request,'myfirstapp/services.html')


def about_us(request):
    return render(request, 'myfirstapp/about_us.html')








import csv
import io

from django.shortcuts import render
from .models import Panier
from .resources import PanierResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset

from .models import Panier
from .resources import PanierResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset
import csv
import io

def panier_list(request):
    paniers = Panier.objects.all()
    imported_objects = []
    error_messages = []

    if request.method == 'POST':
        panier_resource = PanierResource()
        new_paniers = request.FILES.get('myfile')

        # Check if the file is a CSV
        if not new_paniers.name.endswith('.csv'):
            messages.info(request, 'Veuillez télécharger uniquement des fichiers CSV.')
            return render(request, 'myfirstapp/panier_list.html', {'paniers': paniers, 'imported_objects': imported_objects, 'error_messages': error_messages})

        try:
            # Read CSV data using Pandas for simplicity
            data_frame = pd.read_csv(new_paniers)
            
            for _, row in data_frame.iterrows():
                # Update or create Panier objects
                obj, created = Panier.objects.update_or_create(
                    label=row['label'],
                    code=row['code'],
                    description=row['description']
                )
                if created:
                    imported_objects.append(obj)

        except Exception as e:
            error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

    return render(request, 'myfirstapp/panier_list.html', {'paniers': paniers, 'imported_objects': imported_objects, 'error_messages': error_messages})


from django.http import JsonResponse

def export_paniers_csv(request):
    paniers = Panier.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="paniers_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Label', 'Code', 'Description'])

    for panier in paniers:
        writer.writerow([panier.label, panier.code, panier.description])

    return response






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




# myfirstapp/views.py
from .resources import PriceResource, PanierProduitResource
from django.shortcuts import render
from .models import PanierProduit, Price, Panier
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset

def price_list(request):
    prices = Price.objects.all()
    imported_objects = []
    error_messages = []

    if request.method == 'POST':
        new_prices = request.FILES.get('myfile')

        if not new_prices.name.endswith('csv'):
            messages.info(request, 'Veuillez télécharger uniquement des fichiers CSV.')
            return render(request, 'myfirstapp/price_list.html', {'prices': prices, 'imported_objects': imported_objects, 'error_messages': error_messages})

        try:
            data_set = new_prices.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip header row

            for row_number, row in enumerate(csv.reader(io_string, delimiter=',', quotechar="|"), start=2):
                try:
                    if len(row) < 4:
                        raise ValueError(f"La ligne {row_number} ne contient pas suffisamment de colonnes.")

                    value = float(row[0])
                    date = row[1]
                    point_code = row[2]
                    produit_code = row[3]

                    # Try to get PointDeVente by code
                    try:
                        point_instance = PointDeVente.objects.filter(code=point_code).first()
                        if not point_instance:
                            raise ValueError(f"La ligne {row_number}: PointDeVente avec le code {point_code} n'existe pas.")
                    except PointDeVente.MultipleObjectsReturned:
                        # Handle the case where multiple PointDeVente instances have the same code
                        # You might want to log this or handle it according to your application's logic
                        pass

                    # Try to get Produit by code
                    try:
                        produit_instance = Produit.objects.filter(code=produit_code).first()
                        if not produit_instance:
                            raise ValueError(f"La ligne {row_number}: Produit avec le code {produit_code} n'existe pas.")
                    except Produit.MultipleObjectsReturned:
                        # Handle the case where multiple Produit instances have the same code
                        # You might want to log this or handle it according to your application's logic
                        pass

                    obj, created = Price.objects.update_or_create(
                        value=value,
                        date=date,
                        point_ID=point_instance,
                        produit_ID=produit_instance
                    )

                    if created:
                        imported_objects.append(obj)

                except Exception as e:
                    error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

        except Exception as e:
            error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

    return render(request, 'myfirstapp/price_list.html', {'prices': prices, 'imported_objects': imported_objects, 'error_messages': error_messages})


def export_prices_csv(request):
    prices_resource = PriceResource()
    queryset = Price.objects.all()
    dataset = prices_resource.export(queryset)
    
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prices_export.csv"'
    
    return response




def export_prices_csv(request):
    prices_resource = PriceResource()
    queryset = Price.objects.all()
    dataset = prices_resource.export(queryset)
    
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prices_export.csv"'
    
    return response



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



























# myfirstapp/views.py
from import_export import resources
from .resources import ProduitResource
from .models import Produit, FamilleProduit
from django.shortcuts import render, redirect
from django.contrib import messages
from tablib import Dataset
import csv
import io
import chardet  # Import chardet for encoding detection


def produit_list(request):
    produits = Produit.objects.all()
    imported_objects = []
    error_messages = []

    if request.method == 'POST':
        produit_resource = ProduitResource()
        dataset = Dataset()
        new_produits = request.FILES.get('myfile')

        if not new_produits.name.endswith('csv'):
            messages.info(request, 'Veuillez télécharger uniquement des fichiers CSV.')
            return render(request, 'myfirstapp/produit_list.html', {'produits': produits, 'imported_objects': imported_objects, 'error_messages': error_messages})

        try:
            # Detect file encoding
            rawdata = new_produits.read()
            result = chardet.detect(rawdata)
            encoding = result['encoding']

            # Use the detected encoding for decoding
            data_set = rawdata.decode(encoding)
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip header row

            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                # Ensure that FamilleProduit with label=column[3] exists before creating Produit
                famille_produit, created = FamilleProduit.objects.get_or_create(label=column[3])

                obj, created = Produit.objects.update_or_create(
                    label=column[0],
                    price_unit=column[1],
                    code=column[2],
                    famille_produit_ID=famille_produit
                )
                if created:
                    imported_objects.append(obj)

        except Exception as e:
            error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

    return render(request, 'myfirstapp/produit_list.html', {'produits': produits, 'imported_objects': imported_objects, 'error_messages': error_messages})

def export_produits_csv(request):
    produit_resource = ProduitResource()
    dataset = produit_resource.export(Produit.objects.all())
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="produits.csv"'
    return response





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

from .resources import FamilleProduitResource

from django.shortcuts import render
from .models import FamilleProduit
from .resources import FamilleProduitResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset
import csv, io



def famille_produit_list(request):
    famille_produits = FamilleProduit.objects.all()
    imported_objects = []
    error_messages = []

    if request.method == 'POST':
        famille_produit_resource = FamilleProduitResource()
        dataset = Dataset()
        new_famille_produits = request.FILES.get('myfile')

        if not new_famille_produits.name.endswith('csv'):
            messages.info(request, 'Veuillez télécharger uniquement des fichiers CSV.')
            return render(request, 'myfirstapp/famille_produit_list.html', {'famille_produits': famille_produits, 'imported_objects': imported_objects, 'error_messages': error_messages})

        try:
            data_set = new_famille_produits.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip header row

            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                obj, created = FamilleProduit.objects.update_or_create(
                    label=column[0]
                )
                if created:
                    imported_objects.append(obj)

        except Exception as e:
            error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

    return render(request, 'myfirstapp/famille_produit_list.html', {'famille_produits': famille_produits, 'imported_objects': imported_objects, 'error_messages': error_messages})



# views.py

def export_famille_produits_csv(request):
    famille_produit_resource = FamilleProduitResource()
    dataset = famille_produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="famille_produits.csv"'
    return response






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













from django.shortcuts import render, get_object_or_404, redirect
from .models import PointDeVente
from .forms import PointDeVenteForm
from import_export import resources
from tablib import Dataset
from django.http import HttpResponse

class PointDeVenteResource(resources.ModelResource):
    class Meta:
        model = PointDeVente
        skip_unchanged = True
        report_skipped = False
        fields = ('code', 'wilaya', 'moughataa', 'commune', 'gps_lat', 'gps_long')

def point_de_vente_list(request):
    points_de_vente = PointDeVente.objects.all()
    imported_objects = []
    error_messages = []

    if request.method == 'POST':
        point_de_vente_resource = PointDeVenteResource()
        dataset = Dataset()
        new_points_de_vente = request.FILES.get('myfile')

        if not new_points_de_vente.name.endswith('csv'):
            messages.info(request, 'Veuillez télécharger uniquement des fichiers CSV.')
            return render(request, 'myfirstapp/point_de_vente_list.html', {'points_de_vente': points_de_vente, 'imported_objects': imported_objects, 'error_messages': error_messages})

        try:
            data_set = new_points_de_vente.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip header row

            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                obj, created = PointDeVente.objects.update_or_create(
                    code=column[0],
                    wilaya=column[1],
                    moughataa=column[2],
                    commune=column[3],
                    gps_lat=column[4],
                    gps_long=column[5]
                )
                if created:
                    imported_objects.append(obj)

        except Exception as e:
            error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

    return render(request, 'myfirstapp/point_de_vente_list.html', {'points_de_vente': points_de_vente, 'imported_objects': imported_objects, 'error_messages': error_messages})

def export_points_de_vente_csv(request):
    point_de_vente_resource = PointDeVenteResource()
    dataset = point_de_vente_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="points_de_vente.csv"'
    return response





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













from django.shortcuts import render
from .models import PanierProduit
from .resources import PanierProduitResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset
import csv, io


from django.shortcuts import render
from .models import PanierProduit, Price, Panier
from .resources import PanierProduitResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset
import csv, io

from .forms import PanierProduitForm


# myfirstapp/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import PanierProduit, Price, Panier
from django.contrib import messages


def panier_produit_list(request):
    error_messages = []

    if request.method == 'POST':
        dataset = Dataset()
        new_panier_produits = request.FILES.get('myfile')

        if not new_panier_produits.name.endswith('csv'):
            messages.info(request, 'Veuillez télécharger uniquement des fichiers CSV.')
            return render(request, 'myfirstapp/panier_produit_list.html', {'panier_produits': PanierProduit.objects.all(), 'error_messages': error_messages})

        try:
            data_set = new_panier_produits.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)  # Skip header row

            for row_number, row in enumerate(csv.reader(io_string, delimiter=',', quotechar="|"), start=2):
                try:
                    if len(row) < 3:
                        raise ValueError(f"La ligne {row_number} ne contient pas suffisamment de colonnes.")

                    price_id = int(row[0])
                    panier_id = int(row[1])
                    ponderation = float(row[2])

                    # Handle non-existing Price ID gracefully
                    try:
                        price_instance = Price.objects.get(id=price_id)
                    except Price.DoesNotExist:
                        # Log a message or skip the row as needed
                        error_messages.append(f"La ligne {row_number}: Price avec l'ID {price_id} n'existe pas.")
                        continue
                    except Price.MultipleObjectsReturned:
                        # Handle the case where multiple Price instances have the same ID
                        pass

                    panier_instance = Panier.objects.get(id=panier_id)

                    PanierProduit.objects.create(
                        price_ID=price_instance,
                        panier_ID=panier_instance,
                        ponderation=ponderation
                    )
                except Exception as e:
                    error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

            messages.success(request, 'Importation réussie!')
            return render(request, 'myfirstapp/panier_produit_list.html', {'panier_produits': PanierProduit.objects.all(), 'error_messages': error_messages})
        except Exception as e:
            error_messages.append(f"Erreur lors de la lecture du fichier : {e}")

    return render(request, 'myfirstapp/panier_produit_list.html', {'panier_produits': PanierProduit.objects.all(), 'error_messages': error_messages})


def panier_produit_export(request):
    panier_produit_resource = PanierProduitResource()
    dataset = panier_produit_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="panier_produits.csv"'
    return response



def panier_produit_detail(request, pk):
    panier_produit = get_object_or_404(PanierProduit, pk=pk)
    return render(request, 'myfirstapp/panier_produit_detail.html', {'panier_produit': panier_produit})

def panier_produit_new(request):
    if request.method == "POST":
        form = PanierProduitForm(request.POST)
        if form.is_valid():
            panier_produit = form.save(commit=False)
            panier_produit.save()
            return redirect('panier_produit_detail', pk=panier_produit.pk)
    else:
        form = PanierProduitForm()
    return render(request, 'myfirstapp/panier_produit_edit.html', {'form': form})

def panier_produit_edit(request, pk):
    panier_produit = get_object_or_404(PanierProduit, pk=pk)
    if request.method == "POST":
        form = PanierProduitForm(request.POST, instance=panier_produit)
        if form.is_valid():
            panier_produit = form.save(commit=False)
            panier_produit.save()
            return redirect('panier_produit_detail', pk=panier_produit.pk)
    else:
        form = PanierProduitForm(instance=panier_produit)
    return render(request, 'myfirstapp/panier_produit_edit.html', {'form': form})

def panier_produit_delete(request, pk):
    panier_produit = get_object_or_404(PanierProduit, pk=pk)
    panier_produit.delete()
    return redirect('panier_produit_list')






from django.shortcuts import render
from .models import INPC

def inpc_view(request):
    inpc_data = INPC.objects.all()
    return render(request, 'myfirstapp/visualisation.html', {'inpc_data': inpc_data})














# myfirstapp/views.py
from django.shortcuts import render
from .forms import PredictionForm
from sklearn.linear_model import LinearRegression
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split

def train_linear_regression_model():
    data_inpc = {'Mois': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
                 '2016': [100.7, 100.3, 100.6, 100.8, 101.1, 101.6, 102.0, 103.2, 104.3, 105.1, 104.9, 104.7],
                 '2017': [103.9, 103.7, 103.7, 103.8, 104.0, 104.1, 104.5, 105.5, 105.9, 106.0, 106.2, 106.0],
                 '2018': [106.5, 106.5, 107.1, 107.2, 107.4, 107.8, 108.1, 108.6, 109.1, 108.9, 109.1, 109.3],
                 '2019': [109.1, 109.0, 109.1, 109.1, 109.3, 109.7, 110.5, 111.2, 111.7, 112.0, 112.5, 112.3],
                 '2020': [112.2, 112.4, 112.6, 112.6, 112.7, 112.9, 112.8, 112.9, 113.4, 113.6, 114.6, 114.3],
                 '2021': [114.7, 115.2, 115.3, 115.4, 115.7, 116.1, 116.8, 117.9, 118.7, 118.9, 119.9, 120.8],
                 '2022': [110.1, 110.6, 111.5, 113.0, 114.1, 115.2, 116.9, 118.5, 119.5, 121.3, 121.7, 121.4],
                 '2023': [121.4, 120.6, 120.6, 120.5, 121.0, 121.1, 121.6, 122.9, 123.1, 123.4, 123.2, 123.5]}

    df_inpc = pd.DataFrame(data_inpc)
    mois_francais = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    df_inpc['Mois_Num'] = df_inpc['Mois'].apply(lambda x: mois_francais.index(x.lower()) + 1)

    train_data, _ = train_test_split(df_inpc, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(train_data[['2016', '2017', '2018', '2019', '2020', '2021', '2022', 'Mois_Num']], train_data['2023'])
    return model, df_inpc

# Load the model and df_inpc when the module is imported
model, df_inpc = train_linear_regression_model()

def predict_inpc(date):
    prediction_date = datetime.strptime(date, "%m/%d/%Y")

    month_values = pd.DataFrame({
        '2016': [df_inpc.at[0, '2016']],
        '2017': [df_inpc.at[0, '2017']],
        '2018': [df_inpc.at[0, '2018']],
        '2019': [df_inpc.at[0, '2019']],
        '2020': [df_inpc.at[0, '2020']],
        '2021': [df_inpc.at[0, '2021']],
        '2022': [df_inpc.at[0, '2022']],
        'Mois_Num': [prediction_date.month]
    })

    prediction = model.predict(month_values[['2016', '2017', '2018', '2019', '2020', '2021', '2022', 'Mois_Num']])
    return prediction[0]

def inpc_view1(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction_date = form.cleaned_data['prediction_date']
            predicted_inpc = predict_inpc(prediction_date.strftime('%m/%d/%Y'))
            return render(request, 'myfirstapp/prediction.html', {'predicted_inpc': predicted_inpc, 'form': form})
    else:
        form = PredictionForm()

    return render(request, 'myfirstapp/prediction.html', {'form': form})








def visualisation_view(request):
    # Assuming you have some logic to retrieve inpc_data
    inpc_data = get_inpc_data()

    return render(request, 'myfirstapp/visualisation.html', {'inpc_data': inpc_data})



from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import INPC

def inpc_view(request):
    inpc_data = INPC.objects.all()

    # Check if the user wants to download CSV
    if 'download_csv' in request.GET:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="donnees_inpc.csv"'

        writer = csv.writer(response)
        writer.writerow(['Mois', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'])

        # Add your data to export here
        for data in inpc_data:
            writer.writerow([data.mois, data.annee_2016, data.annee_2017, data.annee_2018, data.annee_2019, data.annee_2020, data.annee_2021, data.annee_2022, data.annee_2023])

        return response

    return render(request, 'myfirstapp/visualisation.html', {'inpc_data': inpc_data})



# views.py

from django.http import HttpResponse
import csv
from .models import INPC

def export_csv_view(request):
    inpc_data = INPC.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="donnees_inpc.csv"'

    writer = csv.writer(response)
    writer.writerow(['Mois', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'])

    # Add your data to export here
    for data in inpc_data:
        writer.writerow([data.mois, data.annee_2016, data.annee_2017, data.annee_2018, data.annee_2019, data.annee_2020, data.annee_2021, data.annee_2022, data.annee_2023])

    return response




# views.py

from django.shortcuts import render
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from .models import INPC

def inpc_graphs_view(request):
    # Récupérer les données de la base de données ou utilisez les données en dur
    inpc_data = INPC.objects.all()

    # Créer un DataFrame avec les données
    df_inpc = pd.DataFrame(list(inpc_data.values()))

    # Convertir les noms de colonnes en minuscules
    df_inpc.columns = [col.lower() for col in df_inpc.columns]

    # Imprimer les noms des colonnes
    print(df_inpc.columns)

    # Graphique interactif Plotly pour l'évolution de l'INPC par mois
    fig1 = px.line(df_inpc, x='mois', y=df_inpc.columns[2:], title='Évolution de l\'INPC par mois (2016-2023)',
                   labels={'value': 'INPC', 'variable': 'Année'})

    # Graphique Seaborn pour l'évolution de l'INPC par mois
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_inpc.melt(id_vars='mois'), x='mois', y='value', hue='variable')
    plt.title('Évolution de l\'INPC par mois (2016-2023)')
    plt.xlabel('Mois')
    plt.ylabel('INPC')
    plt.legend(title='Année')

    # Graphique interactif Plotly pour l'évolution de l'INPC par année
    fig2 = px.line(df_inpc, x='mois', y=df_inpc.columns[2:], title='Évolution de l\'INPC par année (2016-2023)',
                   labels={'value': 'INPC', 'variable': 'Année'}, animation_frame='mois')

    # Graphique à barres pour représenter les valeurs INPC par année
    fig3 = px.bar(df_inpc.melt(id_vars=['mois'], value_vars=df_inpc.columns[2:]),
                  x='mois', y='value', color='variable',
                  title='Valeurs INPC par année (2016-2023)')

    # Graphique en nuage de points pour montrer la corrélation entre les années
    fig4 = px.scatter(df_inpc.melt(id_vars=['mois'], value_vars=df_inpc.columns[2:]),
                      x='mois', y='value', color='variable',
                      title='Corrélation entre les années (2016-2023)')

    # Exclure le tracé de la colonne 'id' dans les graphiques 3 et 4
    fig3.for_each_trace(lambda t: t.update(name=t.name.split('=')[1] if 'id' in t.name else t.name))
    fig4.for_each_trace(lambda t: t.update(name=t.name.split('=')[1] if 'id' in t.name else t.name))

    # Rendre les graphiques en format HTML
    graph1_html = fig1.to_html(full_html=False)
    graph2_html = fig2.to_html(full_html=False)
    graph3_html = fig3.to_html(full_html=False)
    graph4_html = fig4.to_html(full_html=False)

    return render(request, 'myfirstapp/inpc_graphs.html', {
        'graph1_html': graph1_html,
        'graph2_html': graph2_html,
        'graph3_html': graph3_html,
        'graph4_html': graph4_html
    })
    
    
    






# views.py
from django.shortcuts import render
from django.http import JsonResponse
from myfirstapp.models import Price
from datetime import datetime, timedelta

# def price_chart(request, produit_id):
#     # Récupérer les dates de début et de fin à partir des paramètres GET
#     start_date_param = request.GET.get('start_date', None)
#     end_date_param = request.GET.get('end_date', None)

#     # Définir des dates par défaut si elles ne sont pas fournies
#     start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else datetime.now() - timedelta(days=365)
#     end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else datetime.now()

#     # Récupérer les prix spécifiques au produit et les trier par date
#     prices = Price.objects.filter(produit_ID__id=produit_id, date__range=(start_date, end_date)).order_by('date')

#     # Préparer les données pour le graphique
#     data = {
#         'labels': [price.date for price in prices],
#         'data': [price.value for price in prices],
#     }

#     return JsonResponse(data)

# def price_chart_page(request, produit_id):
#     return render(request, 'myfirstapp/price_chart.html', {'produit_id': produit_id})



# views.py
from django.shortcuts import render
from django.http import JsonResponse
from myfirstapp.models import Price
from datetime import datetime, timedelta

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from myfirstapp.models import Price
from datetime import datetime, timedelta

def price_chart(request, produit_id):
    # Récupérer les dates de début et de fin à partir des paramètres GET
    start_date_param = request.GET.get('start_date', None)
    end_date_param = request.GET.get('end_date', None)

    # Définir des dates par défaut si elles ne sont pas fournies
    start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else datetime.now() - timedelta(days=365)
    end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else datetime.now()

    # Récupérer les prix spécifiques au produit et les trier par date
    prices = Price.objects.filter(produit_ID__id=produit_id, date__range=(start_date, end_date)).order_by('date')

    # Préparer les données pour le graphique
    data = {
        'labels': [price.date for price in prices],
        'data': [price.value for price in prices],
    }

    return JsonResponse(data)

def price_chart_page(request, produit_id):
    return render(request, 'myfirstapp/price_chart.html', {'produit_id': produit_id})









from django.shortcuts import render, redirect
from myfirstapp.models import Produit
from django.shortcuts import render
from myfirstapp.models import Produit
# views.py
from django.shortcuts import render, redirect
from myfirstapp.models import Produit

def choose_product(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')
        if produit_id:
            # Redirect to the price_chart view with the selected produit_id
            return redirect('price_chart', produit_id=produit_id)

    # Utilisez distinct() sur le champ label pour obtenir des produits distincts
    produits = Produit.objects.values('label',"id").distinct()
    return render(request, 'myfirstapp/choose_product.html', {'produits': produits})





