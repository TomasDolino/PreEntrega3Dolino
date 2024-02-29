from django import forms
from .models import *

class AlquilarForm(forms.ModelForm):
    # Formulario específico para la creación de propiedades en alquiler
    class Meta:
        model = Alquilar  # Especifica el modelo al que está vinculado el formulario
        fields = ['tipo', 'mt2', 'precio']  # Campos del modelo incluidos en el formulario

class ComprarForm(forms.ModelForm):
    # Formulario específico para la creación de propiedades en venta
    class Meta:
        model = Comprar  # Especifica el modelo al que está vinculado el formulario
        fields = ['tipo', 'mt2', 'precio']  # Campos del modelo incluidos en el formulario

class tasarForm(forms.Form):
    # Formulario para solicitar la tasación de una propiedad
    tipo = forms.CharField(max_length=50, required=True)  # Campo para el tipo de propiedad
    mt2 = forms.IntegerField(required=True)  # Campo para los metros cuadrados de la propiedad
    precio = forms.IntegerField(required=True)  # Campo para el precio estimado de la propiedad