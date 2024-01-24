
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import panier_produit_export
from . import views 
from django.urls import path
from .views import export_produits_csv
from .views import choose_product , price_chart , price_chart_page
from .views import (
    panier_list,export_prices_csv ,generate_pdf, panier_produit_export , visualisation_view ,export_produits_csv,export_famille_produits_csv , export_points_de_vente_csv ,export_paniers_csv, about_us, inpc_graphs_view  ,export_csv_view ,panier_detail, panier_new, panier_edit, panier_delete,
    price_list, price_detail, price_new, price_edit, price_delete,
    produit_list, produit_detail, produit_new, produit_edit, produit_delete,
    famille_produit_list, famille_produit_detail, famille_produit_new, famille_produit_edit, famille_produit_delete,
    point_de_vente_list, point_de_vente_detail, point_de_vente_new, point_de_vente_edit, point_de_vente_delete,panier_produit_list,
    panier_produit_detail, panier_produit_new,panier_produit_edit, panier_produit_delete,inpc_view,inpc_view1 ,
)



urlpatterns = [

    
    
    
    
    
    path('download-pdf/', generate_pdf, name='download_pdf'),
    
    path('', views.accueil, name='accueil'),
    path('services/',views.services,name='services'),
    path('about_us/', about_us, name='about_us'),
    
    
    path('price-chart/<int:produit_id>/', price_chart, name='price_chart'),

    path('price-chart-page/<int:produit_id>/', views.price_chart_page, name='price_chart_page'),
    
    path('chart/', choose_product, name='choose_product'),
    

    # path('price-chart-page/<int:produit_id>/', price_chart_page, name='price_chart_page'),





    path('panier/', views.panier_list, name='panier_list'), 
    path('panier/<int:pk>/', views.panier_detail, name='panier_detail'),
    path('panier/new/', views.panier_new, name='panier_new'),
    path('panier/<int:pk>/edit/', views.panier_edit, name='panier_edit'),
    path('panier/<int:pk>/delete/', views.panier_delete, name='panier_delete'),
    path('export_paniers_csv/', export_paniers_csv, name='export_paniers_csv'),
    
    
    

    # URL pour Price
    path('price/', views.price_list, name='price_list'),
    path('price/<int:pk>/', views.price_detail, name='price_detail'),
    path('price/new/', views.price_new, name='price_new'),
    path('price/<int:pk>/edit/', views.price_edit, name='price_edit'),
    path('price/<int:pk>/delete/', views.price_delete, name='price_delete'),
    path('export_prices_csv/', views.export_prices_csv, name='export_prices_csv'),
    
    

    # URL pour Produit
    path('produit/', views.produit_list, name='produit_list'),
    path('produit/<int:pk>/', views.produit_detail, name='produit_detail'),
    path('produit/new/', views.produit_new, name='produit_new'),
    path('produit/<int:pk>/edit/', views.produit_edit, name='produit_edit'),
    path('produit/<int:pk>/delete/', views.produit_delete, name='produit_delete'),
    path('export_produits_csv/', views.export_produits_csv, name='export_produits_csv'),
    
    

    # URL pour FamilleProduit
    path('famille-produit/', views.famille_produit_list, name='famille_produit_list'),
    path('famille-produit/<int:pk>/', views.famille_produit_detail, name='famille_produit_detail'),
    path('famille-produit/new/', views.famille_produit_new, name='famille_produit_new'),
    path('famille-produit/<int:pk>/edit/', views.famille_produit_edit, name='famille_produit_edit'),
    path('famille-produit/<int:pk>/delete/', views.famille_produit_delete, name='famille_produit_delete'),
    path('export_famille_produits_csv/', views.export_famille_produits_csv, name='export_famille_produits_csv'),


    # URL pour PointDeVente
    path('point-de-vente/', views.point_de_vente_list, name='point_de_vente_list'),
    path('point-de-vente/<int:pk>/', views.point_de_vente_detail, name='point_de_vente_detail'),
    path('point-de-vente/new/', views.point_de_vente_new, name='point_de_vente_new'),
    path('point-de-vente/<int:pk>/edit/', views.point_de_vente_edit, name='point_de_vente_edit'),
    path('point-de-vente/<int:pk>/delete/', views.point_de_vente_delete, name='point_de_vente_delete'),
    path('export_points_de_vente_csv/', views.export_points_de_vente_csv, name='export_points_de_vente_csv'),
    
    
    
    # URL pour panier_produit
    path('panier_produit/', panier_produit_list, name='panier_produit_list'),
    path('panier_produit/<int:pk>/', panier_produit_detail, name='panier_produit_detail'),
    path('panier_produit/new/', panier_produit_new, name='panier_produit_new'),
    path('panier_produit/<int:pk>/edit/', panier_produit_edit, name='panier_produit_edit'),
    path('panier_produit/<int:pk>/delete/', panier_produit_delete, name='panier_produit_delete'),
    path('panier_produit_export/', views.panier_produit_export, name='panier_produit_export'),
    
    
    
    
    
    
    
    path('predict/', inpc_view1, name='inpc_view1'),
    
    path('inpc/', inpc_view, name='inpc_view'),
    
    path('export_csv/', export_csv_view, name='export_csv'),
    
    
    path('inpc_graphs/', inpc_graphs_view, name='inpc_graphs'),
    path('visualisation/', visualisation_view, name='visualisation'),
    
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



