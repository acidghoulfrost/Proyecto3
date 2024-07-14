import datetime
from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=7, verbose_name="Rut")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    correo = models.EmailField(max_length=200, verbose_name="Correo")
    num_telefono = models.IntegerField()

    def __str__(self):
        return self.rut
    
class Cajas(models.Model):
    id_caja = models.AutoField(primary_key=True)
    tipo_caja = models.CharField(max_length=25)
    peso = models.IntegerField()
    dimension = models.CharField(max_length=10)

    def __str__(self):
        return self.id_caja
    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField(default=0)
    fecha_compra = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)

    def __str__(self):
        return self.id_boleta
    
class Detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_caja = models.ForeignKey('Cajas', blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)