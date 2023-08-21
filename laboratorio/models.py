from django.db import models

from django.core.exceptions import ValidationError

# Create your models here.

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

def validar_anio(value):
    if value < 2015:
        raise ValidationError(('La fecha de fabricación debe ser a partir de 2015'))


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.IntegerField(validators=[validar_anio])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre