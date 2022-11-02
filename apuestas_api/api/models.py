from django.db import models

# Create your models here.
class Cuota(models.Model):
    partido = models.CharField(max_length=100)
    pronostico= models.CharField(max_length=100)
    cuota = models.DecimalField(max_digits=3, decimal_places=2)

class Ayer(models.Model):
    partido = models.CharField(max_length=100)
    pronostico= models.CharField(max_length=100)
    cuota = models.DecimalField(max_digits=3, decimal_places=2)
    resultado = models.BooleanField()
