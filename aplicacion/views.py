from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Vista de la página de inicio
def home(request):
    # Renderiza la plantilla home.html
    return render(request, 'aplicacion/home.html')

# Vista para listar y agregar propiedades de alquiler
@login_required  # Requiere que el usuario esté autenticado
def alquilar(request):
    # Procesa el formulario de alquiler si se envía con el método POST
    if request.method == 'POST':
        form = AlquilarForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva propiedad de alquiler en la base de datos
            return redirect('alquilar')  # Redirige a la lista de alquileres
    else:
        form = AlquilarForm()
    alquilar = Alquilar.objects.all()  # Obtiene todas las propiedades de alquiler de la base de datos
    # Renderiza la plantilla alquilar.html con las propiedades de alquiler y el formulario
    return render(request, 'aplicacion/alquilar.html', {'alquilar': alquilar, 'form': form})

# Vista para agregar una nueva propiedad de alquiler
@login_required
def alquilar_agregar(request):
    if request.method == 'POST':
        form = AlquilarForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la propiedad en la base de datos
            return redirect('alquilar')  # Redirige a la lista de alquileres
    else:
        form = AlquilarForm()
    # Renderiza la plantilla alquilar_agregar.html con el formulario
    return render(request, 'aplicacion/alquilar_agregar.html', {'form': form})

# Vista para editar una propiedad de alquiler existente
@login_required
def alquilar_editar(request, id):
    # Obtiene la propiedad de alquiler por ID o devuelve un error 404 si no existe
    propiedad = get_object_or_404(Alquilar, id=id)
    if request.method == 'POST':
        form = AlquilarForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()  # Guarda los cambios en la propiedad
            return redirect('alquilar')  # Redirige a la lista de alquileres
    else:
        form = AlquilarForm(instance=propiedad)
    # Renderiza la plantilla alquilar_editar.html con el formulario y la propiedad a editar
    return render(request, 'aplicacion/alquilar_editar.html', {'form': form, 'propiedad': propiedad})

# Vista para borrar una propiedad de alquiler
@login_required
def alquilar_borrar(request, id):
    propiedad = get_object_or_404(Alquilar, id=id)
    if request.method == 'POST':
        propiedad.delete()  # Elimina la propiedad de la base de datos
        return redirect('alquilar')  # Redirige a la lista de alquileres
    # Renderiza la plantilla alquilar_borrar.html con la propiedad a borrar
    return render(request, 'aplicacion/alquilar_borrar.html', {'propiedad': propiedad})

# Vista para listar y agregar propiedades de compra
@login_required
def comprar(request):
    if request.method == 'POST':
        form = ComprarForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda la nueva propiedad de compra
            return redirect('comprar')  # Redirige a la lista de compras
    else:
        form = ComprarForm()
    comprar = Comprar.objects.all()  # Obtiene todas las propiedades de compra
    # Renderiza la plantilla comprar.html con las propiedades de compra y el formulario
    return render(request, 'aplicacion/comprar.html', {'comprar': comprar, 'form': form})

# Vista para editar una propiedad de compra existente
@login_required
def comprar_editar(request, id):
    propiedad = get_object_or_404(Comprar, id=id)
    if request.method == 'POST':
        form = ComprarForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()  # Guarda los cambios en la propiedad
            return redirect('comprar')  # Redirige a la lista de compras
    else:
        form = ComprarForm(instance=propiedad)
    # Renderiza la plantilla comprar_editar.html con el formulario y la propiedad a editar
    return render(request, 'aplicacion/comprar_editar.html', {'form': form, 'propiedad': propiedad})

# Vista para borrar una propiedad de compra
@login_required
def comprar_borrar(request, id):
    propiedad = get_object_or_404(Comprar, id=id)
    if request.method == 'POST':
        propiedad.delete()  # Elimina la propiedad de la base de datos
        return redirect('comprar')  # Redirige a la lista de compras
    # Renderiza la plantilla comprar_borrar.html con la propiedad a borrar
    return render(request, 'aplicacion/comprar_borrar.html', {'propiedad': propiedad})

# Vista para solicitar tasación de una propiedad
def tasar(request):
    if request.method == 'POST':
        form = tasarForm(request.POST)
        if form.is_valid():
            # No guarda en base de datos, solo muestra mensaje de éxito
            messages.success(request, 'Tu solicitud ha sido enviada. Te contestaremos a la brevedad.')
            return redirect('tasar')  # Redirige a la vista de tasación
    else:
        form = tasarForm()
    contexto = {'form': form}
    # Renderiza la plantilla tasar.html con el formulario de tasación
    return render(request, 'aplicacion/tasar.html', contexto)

# Vista para procesar el formulario de propiedades y redirigir según la operación seleccionada
def propiedades_Form(request):
    if request.method == 'POST':
        form = propiedadesForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y crea una nueva propiedad según la operación seleccionada
            tipo = form.cleaned_data['tipo']
            mt2 = form.cleaned_data['mt2']
            precio = form.cleaned_data['precio']
            operacion = form.cleaned_data['operacion']
            # Crea y guarda la propiedad en la base de datos según el tipo de operación
            if operacion == 'alquiler':
                nueva_propiedad = Alquilar(tipo=tipo, mt2=mt2, precio=precio)
                nueva_propiedad.save()
            elif operacion == 'comprar':
                nueva_propiedad = Comprar(tipo=tipo, mt2=mt2, precio=precio)
                nueva_propiedad.save()
            elif operacion == 'tasar':
                nueva_propiedad = Tasar(tipo=tipo, mt2=mt2, precio=precio)
                nueva_propiedad.save()
            return redirect('propiedades_form')  # Redirige al formulario de propiedades
    else:
        form = propiedadesForm()
    # Renderiza la plantilla propiedades_form.html con el formulario de propiedades
    return render(request, 'aplicacion/propiedades_form.html', {'form': form})

# Vista para buscar oportunidades de alquiler o compra
def buscar(request):
    # Renderiza la plantilla buscar.html
    return render(request, 'aplicacion/buscar.html')

# Vista para mostrar resultados de búsqueda según el tipo de operación y propiedad
def buscarOportunidad(request):
    tipo_operacion = request.GET.get('tipo_operacion')
    tipo_propiedad = request.GET.get('tipo_propiedad')
    # Filtra las propiedades según el tipo de operación y propiedad
    if tipo_operacion == 'alquilar':
        resultados = Alquilar.objects.filter(tipo__icontains=tipo_propiedad)
    elif tipo_operacion == 'comprar':
        resultados = Comprar.objects.filter(tipo__icontains=tipo_propiedad)
    else:
        resultados = []
    contexto = {'resultados': resultados, 'tipo_operacion': tipo_operacion}
    # Renderiza la plantilla resultados_busqueda.html con los resultados de búsqueda
    return render(request, 'aplicacion/resultados_busqueda.html', contexto)

# Vista para la página "Sobre mí"
def about_me(request):
    # Renderiza la plantilla about_me.html
    return render(request, 'aplicacion/about_me.html')