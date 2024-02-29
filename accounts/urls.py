from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Registro de nuevos usuarios
    path('login/', views.login_view, name='login'),  # Inicio de sesión
    path('logout/', views.logout_view, name='logout'),  # Cierre de sesión
    path('profile/', views.profile, name='profile'),  # Mostrar perfil del usuario
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Editar perfil del usuario
]