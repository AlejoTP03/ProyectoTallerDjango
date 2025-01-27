from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home, name = 'home'),
    
    path('mecanicos/', mecanico_list, name='mecanico_list'),
    path('mecanicos/new/', mecanico_create, name='mecanico_create'),
    path('mecanicos/edit/<int:pk>/', mecanico_update, name='mecanico_update'),
    path('mecanicos/delete/<int:pk>/', mecanico_delete, name='mecanico_delete'),
    
    path('carros/', carros_list, name= 'carros_list'),
    path('carros/new/', carro_create, name='carro_create'),
    path('carros/edit/<int:pk>/', carro_update, name='carro_update'),
    path('carros/delete/<int:pk>/', carro_delete, name='carro_delete'),
    
    path('propietarios/', propietario_list, name= 'propietario_list'),
    path('propietarios/new/', propietario_create, name='propietario_create'),
    path('propietarios/edit/<int:pk>/', propietario_update, name='propietario_update'),
    path('propietarios/delete/<int:pk>/', propietario_delete, name='propietario_delete'),
    
    path('carros/home.html', home, name= 'home'),
    path('mecanicos/home.html', home, name= 'home'),
    path('propietarios/home.html', home, name= 'home'),
    
]
