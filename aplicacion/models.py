from django.db import models


class Alquilar(models.Model):
    # Modelo para las propiedades disponibles para alquilar
    tipo = models.CharField(max_length=50)  # Tipo de propiedad (ej. casa, departamento)
    mt2 = models.IntegerField()  # Metros cuadrados de la propiedad
    precio = models.IntegerField(default=0)  # Precio de alquiler de la propiedad
    
    def __str__(self):
        # Representación en cadena del modelo, mostrando el tipo de propiedad
        return f'{self.tipo}'

class Comprar(models.Model):
    # Modelo para las propiedades disponibles para comprar
    tipo = models.CharField(max_length=50)  # Tipo de propiedad (ej. casa, departamento)
    mt2 = models.IntegerField()  # Metros cuadrados de la propiedad
    precio = models.IntegerField()  # Precio de compra de la propiedad
    
    def __str__(self):
        # Representación en cadena del modelo, mostrando el tipo de propiedad
        return f'{self.tipo}'

class Tasar(models.Model):
    # Modelo para las solicitudes de tasación de propiedades
    tipo = models.CharField(max_length=50)  # Tipo de propiedad (ej. casa, departamento)
    mt2 = models.IntegerField()  # Metros cuadrados de la propiedad
    ambientes = models.CharField(max_length=50)  # Número de ambientes de la propiedad

    def __str__(self):
        # Representación en cadena del modelo, mostrando el tipo de propiedad
        return f'{self.tipo}'