from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre
    
class Cajas(models.Model):
    cod_caja = models.CharField(primary_key=True, max_length=5)
    peso = models.CharField(max_length=3)
    empresa = models.CharField(max_length=20)
    precio = models.CharField(max_length=6)
    tipo_caja = models.CharField(max_length=10)

    def __str__(self):
        return self.cod_caja

class Boleta(models.Model):
    id_boleta = models.CharField(primary_key=True, max_length=5)
    nombre_cliente = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.CharField(max_length=40)
    fecha_recepcion = models.DateField()
    fecha_entrega = models.DateField(blank=True, null=True)
    cajas = models.ManyToManyField(Cajas)

    def __str__(self):
        return f'Boleta {self.id_boleta} - {self.nombre_cliente}'