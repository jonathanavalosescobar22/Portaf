from django import forms
from core.models import Libro,Pedido2


class RegistroForm(forms.ModelForm):

    class Meta:
        model = Libro

        fields  = [
            'nombre_solicitante',
            'email_solicitante',
            'nombrelibro',
            'autor',
            'paginas',
            'anio',
            'genero',
            'tipo_despacho',
        ]
        labels = {
            'nombre_solicitante':'Nombre',
            'email_solicitante':'Email',
            'nombrelibro':'Nombre_Libro',
            'autor':'Autor',
            'paginas':'Paginas',
            'anio':'Año',
            'genero':'Genero',
            'tipo_despacho':'Tipo despacho', 
        }
class RegistroPedido(forms.ModelForm):

    class Meta:
        model = Pedido2

        fields  = [
            'nombreclientes',
            'emailclientes',
            'celularcliente',
            'librocliente',
        
        ]
        labels = {
            'nombreclientes':'Nombre',
            'emailclientes':'Email',
            'celularcliente':'Celular',
            'librocliente':'Nombre Libro',
            
        }
        widgets = {
            'nombreclientes': forms.TextInput(attrs={'class':'form-control'}),
            'emailclientes': forms.TextInput(attrs={'class':'form-control'}),
            'celularcliente': forms.TextInput(attrs={'class':'form-control'}),
            'librocliente': forms.Select(attrs={'class':'form-control'}),
            
        }
