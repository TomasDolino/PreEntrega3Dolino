from django.shortcuts import render,redirect, HttpResponse
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,'aplicacion/home.html')

def alquilar(request):
    contexto={'alquilar':Alquilar.objects.all()}
    return render(request,'aplicacion/alquilar.html', contexto)

def alquilar_agregar(request):
    if request.method == 'POST':
        form = Alquilar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alquilar') 
    else:
        form = Alquilar()
    return render(request, 'tu_template_para_agregar.html', {'form': form})

def comprar(request):
    contexto={'comprar':Comprar.objects.all()}
    return render(request,'aplicacion/comprar.html',contexto)

def tasar(request):
    contexto={'tasar':Tasar.objects.all()}
    return render(request,'aplicacion/tasar.html',contexto)

def propiedades_Form(request):
    if request.method == 'POST':
        form = propiedadesForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            mt2 = form.cleaned_data['mt2']
            precio = form.cleaned_data['precio']
            operacion = form.cleaned_data['operacion']

            if operacion == 'alquiler':
                nueva_propiedad = Alquilar(tipo=tipo, mt2=mt2, precio=precio)
                nueva_propiedad.save()              
            elif operacion == 'comprar':
                nueva_propiedad = Comprar(tipo=tipo, mt2=mt2, precio=precio)
                nueva_propiedad.save()
            elif operacion == 'comprar':
                nueva_propiedad = Tasar(tipo=tipo, mt2=mt2, precio=precio)
                nueva_propiedad.save()
            
            return redirect('propiedades_form')
    else:
        form = propiedadesForm()


    return render(request, 'aplicacion/propiedades_form.html', {'form': form})

def buscar(request):
    return render(request, 'aplicacion/buscar.html')

def buscarOportunidad(request):
    tipo_operacion = request.GET.get('tipo_operacion')
    tipo_propiedad = request.GET.get('tipo_propiedad')
    
    if tipo_operacion == 'alquilar':
        resultados = Alquilar.objects.filter(tipo__icontains=tipo_propiedad)
    elif tipo_operacion == 'comprar':
        resultados = Comprar.objects.filter(tipo__icontains=tipo_propiedad)
    else:
        resultados = []
    contexto = {
        'resultados': resultados,
        'tipo_operacion': tipo_operacion
        }
    return render(request, 'aplicacion/resultados_busqueda.html', contexto)
    return HttpResponse('No se ingreso un patro de busqueda valido')