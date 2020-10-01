from django.shortcuts import render
from django.urls import path 
from .views import home,listar_pedidos,guardarpedidos,register,formulario_solicitud,Listarpedido,Listarlibro,guardarmensajes,Listarcomentarios,modificar_pedido
from django.conf.urls import url, include

#putosinvidaalguna

urlpatterns = [
    path('', home, name='home'),
    path('guardarpedidos/',guardarpedidos, name='guardarpedidos'),
    path('listar_pedidos/',listar_pedidos,name='listar_pedidos'),
    path('listar_pedido/',Listarpedido.as_view(),name='listar_pedido'),
    path('Listarlibro/',Listarlibro.as_view(),name='Listarlibro'),
    path('Listarcomentarios/',Listarcomentarios.as_view(),name='Listarcomentarios'),
    path('formulario_solicitud/',formulario_solicitud,name='formulario_solicitud'),
    path('guardarmensajes/',guardarmensajes, name='guardarmensajes'),
    path('register/',register, name='register'),
    path('modificar_pedido/<rut_cliente>/',modificar_pedido, name='modificar_pedido'),
    
    
]