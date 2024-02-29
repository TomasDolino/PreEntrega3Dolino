from .views import *
from django.urls import path, include
from accounts.views import *

urlpatterns = [
    # URL de la página de inicio
    path('', home, name='home'),
    
    # URLs para las vistas relacionadas con alquilar propiedades
    path('alquilar/', alquilar, name='alquilar'),  # Lista y formulario de alquiler
    path('alquilar/agregar/', alquilar_agregar, name='alquilar_agregar'),  # Formulario para agregar nueva propiedad de alquiler
    path('alquilar/editar/<int:id>/', alquilar_editar, name='alquilar_editar'),  # Formulario para editar una propiedad de alquiler
    path('alquilar/borrar/<int:id>/', alquilar_borrar, name='alquilar_borrar'),  # Vista para borrar una propiedad de alquiler
    
    # URLs para las vistas relacionadas con comprar propiedades
    path('comprar/', comprar, name='comprar'),  # Lista y formulario de compra
    path('comprar/editar/<int:id>/', comprar_editar, name='comprar_editar'),  # Formulario para editar una propiedad de compra
    path('comprar/borrar/<int:id>/', comprar_borrar, name='comprar_borrar'),  # Vista para borrar una propiedad de compra
    
    # URL para la vista de tasación de propiedades
    path('tasar/', tasar, name='tasar'),  # Formulario y solicitud de tasación
    
    # URL para el formulario general de propiedades
    path('propiedades_form/', propiedades_Form, name='propiedades_form'),  # Formulario para agregar propiedades según el tipo de operación
    
    # URLs para las vistas de búsqueda
    path('buscar/', buscar, name='buscar'),  # Formulario de búsqueda
    path('buscarOportunidad/', buscarOportunidad, name='buscarOportunidad'),  # Resultados de búsqueda según criterios
    
    # URL para la página "Sobre mí"
    path('about_me/', about_me, name='about_me'),  # Vista de la página "Sobre mí"
]