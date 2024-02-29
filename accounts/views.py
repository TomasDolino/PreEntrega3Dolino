from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *


# Vista de registro de usuario
def signup(request):
    # Procesa el formulario de registro si se envía con el método POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo usuario y lo autentica
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirige al perfil del usuario recién creado
        else:
            # Si el formulario no es válido, muestra los errores
            for field, error in form.errors.items():
                messages.error(request, f"{field}: {error}")
    else:
        # Si no es una petición POST, muestra el formulario de registro vacío
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Vista de inicio de sesión
def login_view(request):
    # Procesa el formulario de inicio de sesión si se envía con el método POST
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            # Si el formulario es válido, autentica al usuario y lo redirige a su perfil
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                # Si la autenticación falla, muestra un mensaje de error
                messages.error(request, "Nombre de usuario o contraseña incorrectos")
    else:
        # Si no es una petición POST, muestra el formulario de inicio de sesión vacío
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form}) 

# Vista de cierre de sesión
def logout_view(request):
    # Cierra la sesión del usuario y lo redirige a la página de inicio de sesión
    logout(request)
    return redirect('login')

# Vista de perfil del usuario
@login_required
def profile(request):
    # Muestra la página de perfil del usuario autenticado
    return render(request, 'accounts/profile.html', {'user': request.user})

# Vista para editar el perfil del usuario
@login_required
def edit_profile(request):
    try:
        # Intenta obtener el perfil del usuario, si no existe, lo crea
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    # Procesa el formulario de edición de perfil si se envía con el método POST
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en el perfil y redirige a la página de perfil
            form.save()
            return redirect('profile')
    else:
        # Si no es una petición POST, muestra el formulario de edición de perfil con la información actual
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


