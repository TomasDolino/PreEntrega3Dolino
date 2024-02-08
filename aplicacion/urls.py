from .views import *
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('alquilar/', alquilar, name='alquilar'),
    path('comprar/', comprar, name='comprar'),
    path('tasar/', tasar, name='tasar'),
    #
    path('propiedades_form/', propiedades_Form, name='propiedades_form'),
    path('buscar/', buscar, name='buscar'),
    path('buscarOportunidad/', buscarOportunidad, name='buscarOportunidad'),
    path('alquilar_agregar/', alquilar_agregar, name='alquilar_agregar'),
]
