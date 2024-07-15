from django.contrib import admin
from .models import Cliente,Producto,Boleta,Detalle_boleta

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Boleta)
admin.site.register(Detalle_boleta)