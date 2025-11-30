from django.urls import path
from . import views

urlpatterns = [

     path('add/', views.add_museum, name='add_museum'),
    path('all/', views.all_del_museum, name='all_del_museum'),
    path('booking/', views.booking, name='booking'),
    path('details/', views.details, name='details'),
    path('search/', views.search, name='search'),

]
 