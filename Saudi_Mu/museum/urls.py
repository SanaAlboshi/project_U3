from django.urls import path
from . import views

urlpatterns = [
    # Add Museum for specific authority
    path('museum/add/<int:authority_id>/', views.add_museum, name='add_museum'),

    path('all/', views.all_del_museum, name='all_del_museum'),

    path('authority/add/', views.add_authority, name='add_authority'),
    path('authority/all/', views.all_authority, name='all_authority'),

    path('booking/', views.booking, name='booking'),
    path('details/', views.details, name='details'),
    path('search/', views.search, name='search'),
]
