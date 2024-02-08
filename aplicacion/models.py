
from django.db import models

# Create your models here.
class Alquilar(models.Model):
    tipo=models.CharField(max_length=50)
    mt2=models.IntegerField()
    precio=models.IntegerField(default=0)
    def __str__(self):
        return f'{self.tipo}'


class Comprar(models.Model):
    tipo=models.CharField(max_length=50)
    mt2=models.IntegerField()
    precio=models.IntegerField()
    def __str__(self):
        return f'{self.tipo}'

class Tasar(models.Model):
    tipo=models.CharField(max_length=50)
    mt2=models.IntegerField()
    ambientes=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tipo}'