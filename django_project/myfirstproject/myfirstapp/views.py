

from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductFamily, Product
from .forms import ProductForm, ProductFamilyForm

def accueil(request):
    return render(request, 'myfirstapp/accueil.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myfirstapp/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myfirstapp/product_detail.html', {'product': product})

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'myfirstapp/product_edit.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'myfirstapp/product_edit.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')




def product_family_list(request):
    product_families = ProductFamily.objects.all()
    return render(request, 'myfirstapp/product_family_list.html', {'product_families': product_families})

def product_family_detail(request, pk):
    product_family = get_object_or_404(ProductFamily, pk=pk)
    return render(request, 'myfirstapp/product_family_detail.html', {'product_family': product_family})

def product_family_new(request):
    if request.method == "POST":
        form = ProductFamilyForm(request.POST)
        if form.is_valid():
            product_family = form.save(commit=False)
            product_family.save()
            return redirect('product_family_detail', pk=product_family.pk)
    else:
        form = ProductFamilyForm()
    return render(request, 'myfirstapp/product_family_edit.html', {'form': form})


def product_family_edit(request, pk):
    product_family = get_object_or_404(ProductFamily, pk=pk)

    if request.method == "POST":
        form = ProductFamilyForm(request.POST, instance=product_family)
        if form.is_valid():
            product_family = form.save(commit=False)
            product_family.save()
            return redirect('product_family_detail', pk=product_family.pk)
    else:
        form = ProductFamilyForm(instance=product_family)

    return render(request, 'myfirstapp/product_family_edit.html', {'form': form, 'product_family': product_family})

def product_family_delete(request, pk):
    product_family = get_object_or_404(ProductFamily, pk=pk)
    product_family.delete()
    return redirect('product_family_list')
