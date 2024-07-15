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
    
class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField(default=0)
    fecha_compra = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)

    def __str__(self):
        return self.id_boleta
    
class Detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)