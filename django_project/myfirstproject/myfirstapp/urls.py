
from . import views 
from django.urls import path
from .views import (
    panier_list, panier_detail, panier_new, panier_edit, panier_delete,
    price_list, price_detail, price_new, price_edit, price_delete,
    produit_list, produit_detail, produit_new, produit_edit, produit_delete,
    famille_produit_list, famille_produit_detail, famille_produit_new, famille_produit_edit, famille_produit_delete,
    point_de_vente_list, point_de_vente_detail, point_de_vente_new, point_de_vente_edit, point_de_vente_delete,
)

urlpatterns = [
    # URL pour Panier
    path('', views.accueil, name='accueil'),
    path('panier/', views.panier_list, name='panier_list'),
    path('panier/<int:pk>/', views.panier_detail, name='panier_detail'),
    path('panier/new/', views.panier_new, name='panier_new'),
    path('panier/<int:pk>/edit/', views.panier_edit, name='panier_edit'),
    path('panier/<int:pk>/delete/', views.panier_delete, name='panier_delete'),

    # URL pour Price
    path('price/', views.price_list, name='price_list'),
    path('price/<int:pk>/', views.price_detail, name='price_detail'),
    path('price/new/', views.price_new, name='price_new'),
    path('price/<int:pk>/edit/', views.price_edit, name='price_edit'),
    path('price/<int:pk>/delete/', views.price_delete, name='price_delete'),

    # URL pour Produit
    path('produit/', views.produit_list, name='produit_list'),
    path('produit/<int:pk>/', views.produit_detail, name='produit_detail'),
    path('produit/new/', views.produit_new, name='produit_new'),
    path('produit/<int:pk>/edit/', views.produit_edit, name='produit_edit'),
    path('produit/<int:pk>/delete/', views.produit_delete, name='produit_delete'),

    # URL pour FamilleProduit
    path('famille-produit/', views.famille_produit_list, name='famille_produit_list'),
    path('famille-produit/<int:pk>/', views.famille_produit_detail, name='famille_produit_detail'),
    path('famille-produit/new/', views.famille_produit_new, name='famille_produit_new'),
    path('famille-produit/<int:pk>/edit/', views.famille_produit_edit, name='famille_produit_edit'),
    path('famille-produit/<int:pk>/delete/', views.famille_produit_delete, name='famille_produit_delete'),

    # URL pour PointDeVente
    path('point-de-vente/', views.point_de_vente_list, name='point_de_vente_list'),
    path('point-de-vente/<int:pk>/', views.point_de_vente_detail, name='point_de_vente_detail'),
    path('point-de-vente/new/', views.point_de_vente_new, name='point_de_vente_new'),
    path('point-de-vente/<int:pk>/edit/', views.point_de_vente_edit, name='point_de_vente_edit'),
    path('point-de-vente/<int:pk>/delete/', views.point_de_vente_delete, name='point_de_vente_delete'),
]





