from django.shortcuts import render, redirect
from .forms import RegistroForm,RegistroPedido
from .models import Genero,Pedido2,Tipo_despacho,Libros,Tipo_pago,Mensaje
from django.views.generic import ListView
from django.urls import reverse_lazy
# comentario
# Create your views here.
class Listarpedido(ListView):
    model = Pedido2
    template_name = 'core/listar_pedido.html'

class Listarlibro(ListView):
    model = Libros
    template_name = 'core/listar_libros.html'

class Listarcomentarios(ListView):
    model = Mensaje
    template_name = 'core/lista_comentarios.html'

#Funciones.
def home(request):
    return render(request, 'core/index.html')


def formulario_solicitud(request):
    return render(request, 'core/formulario_solicitud.html')


# CR PEDIDO,LIBRO
def register(response):
    if response.method == "POST":
	    form = RegistroPedido(response.POST)
	    if form.is_valid():
	        form.save()
	    return redirect("home")
    else:
    	form = RegistroPedido()
    
    return render(response, "core/index.html", {"form":form})

def listar_pedidos(request):

    pedido =    Pedido2.objects.all()
    variables = {'pedidos':pedido}
    return render(request,'core/listar_pedido.html', {'pedidos':variables})


def guardarpedidos(request):
    pedidos = Pedido2.objects.all()   
    variables = {'pedidos':Pedido2}

    if request.POST:
        pedido = Pedido2()
        pedido.rut_cliente = request.POST.get('txtrutSolicitante')
        pedido.nombreclientes = request.POST.get('txtNombreSolicitante')
        pedido.emailclientes = request.POST.get('txtEmail')
        pedido.celularcliente = request.POST.get('txtcelular')
        pedido.librocliente = request.POST.get('txtlibro')
        pedido.tipo_pago = request.POST.get('txttipo_pago')

        try:
            pedido.save()
            variables['mensaje']='Guardado Correctamente'
            
        except:
            variables['mensaje']= 'No se pudo guardar el pedido'

    return render(request, 'core/prueba.html', variables)



def guardarmensajes(request):
    mensaj = Mensaje.objects.all()   
    variables = {'mensajes':mensaj}

    if request.POST:
        mensajee = Mensaje()
        mensajee.nombre = request.POST.get('txtNombre')
        mensajee.mensaje = request.POST.get('txtmensaje')

        try:
            mensajee.save()
            variables['mensaje']='Guardado Correctamente'
            
        except:
            variables['mensaje']= 'No se pudo guardar el pedido'

    return render(request, 'core/mensaje.html', variables)


def  modificar_pedido(request,rut_cliente):

    pedido = Pedido2.objects.get(rut_cliente=rut_cliente)

    variables = {
        'pedido':pedido
    }

    if request.POST:
        pedido = Pedido2()
        pedido.rut_cliente = request.POST.get('txtrutSolicitante')
        pedido.nombreclientes = request.POST.get('txtNombreSolicitante')
        pedido.emailclientes = request.POST.get('txtEmail')
        pedido.celularcliente = request.POST.get('txtcelular')
        pedido.librocliente = request.POST.get('txtlibro')
        pedido.tipo_pago = request.POST.get('txttipo_pago')

        try:
            pedido.save()
            messages.success(request, 'Modificado Correctamente')
        except:
            messages.error(request, 'No se pudo Modificar')
        return redirect('core/listar_pedido.html')


    return render(request, 'core/editar_pedido.html',variables)




