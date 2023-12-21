# myfirstapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('product_list/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    
    path('product_family/', views.product_family_list, name='product_family_list'),
    path('product_family/<int:pk>/' , views.product_family_detail, name='product_family_detail'),
    path('product_family/new/', views.product_family_new, name='product_family_new'),
    path('product_family/<int:pk>/edit/', views.product_family_edit, name='product_family_edit'),
    path('product_family/<int:pk>/delete/', views.product_family_delete, name='product_family_delete'),
    
    
    
]
