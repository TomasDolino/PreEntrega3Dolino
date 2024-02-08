from django import forms
from .models import *

class propiedadesForm(forms.Form):
    tipo = forms.CharField(max_length=50, required=True)
    mt2 = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)
    operacion = forms.ChoiceField(choices=[('alquiler', 'Alquiler'), ('comprar', 'Comprar'),('tasar','Tasar')], required=True)

class AlquilarForm(forms.ModelForm):
    class Meta:
        model = Alquilar
        fields = ['tipo', 'mt2', 'precio']

class ComprarForm(forms.ModelForm):
    class Meta:
        model = Comprar
        fields = ['tipo', 'mt2', 'precio']