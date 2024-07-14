from django.db import models

# Create your models here.

class Cajas(models.Model):
    id_caja=models.CharField(primary_key=True, max_length=8, verbose_name="Codigo Caja")
    tipo_caja= models.CharField(max_length=50, verbose_name="Tipo Caja")
    peso_kg=models.CharField(max_length=50, verbose_name="Peso KG")
    dimension=models.CharField(max_length=50, verbose_name= "Dimension Caja")
    empresa_envio=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    
    def __str__(self):
        return self.id_caja
    
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

class Detalle_boleta(models.Model):
    cod_boleta = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Boleta {self.id_boleta} - {self.nombre_cliente}'