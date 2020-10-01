from django.contrib import admin
from .models import Genero,Pedido2,Tipo_despacho,Libros,Tipo_pago,Mensaje
# Register your models here.

admin.site.register(Genero)
admin.site.register(Pedido2)
admin.site.register(Tipo_despacho)
admin.site.register(Libros)
admin.site.register(Tipo_pago)
admin.site.register(Mensaje)