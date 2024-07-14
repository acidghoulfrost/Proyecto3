from django.contrib import admin
from .models import Cliente,Cajas,Boleta,Detalle_boleta

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Cajas)
admin.site.register(Boleta)
admin.site.register(Detalle_boleta)