from django.contrib import admin

# Register your models here.
# myfirstapp/admin.py

from django.contrib import admin
from .models import ProductFamily, Product
admin.site.register(ProductFamily)
admin.site.register(Product)
