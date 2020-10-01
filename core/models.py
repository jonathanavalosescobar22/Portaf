from django.db import models

objects = models.Manager()

# Create your models here.

class Genero(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Libro(models.Model):

    nombre_solicitante = models.CharField(max_length=50,default="")
    email_solicitante = models.CharField(max_length=50,default="")
    nombrelibro = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    paginas =models.IntegerField()
    anio = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    tipo_despacho = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.nombrelibro


class Tipo_despacho(models.Model):

    nombre_tipo = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.nombre_tipo

class Libros(models.Model):

    nombre_libro = models.CharField(max_length=50)
    autores = models.CharField(max_length=50)
    numeropaginas =models.IntegerField()
    anios = models.IntegerField()
    generos = models.ForeignKey(Genero, on_delete=models.CASCADE)
    tipo_despachos = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.nombre_libro
        

class Tipo_pago(models.Model):

    desc_tipo = models.CharField(max_length=50,default="")

    def __str__(self):
        return self.desc_tipo

class Pedido2(models.Model):

    rut_cliente = models.CharField(max_length=50,default="")
    nombreclientes = models.CharField(max_length=50,default="")
    emailclientes = models.CharField(max_length=50,default="")
    celularcliente = models.IntegerField()
    librocliente =  models.CharField(max_length=50,default="")
    tipo_pago =  models.CharField(max_length=50,default="")

    def __str__(self):
        return self.nombreclientes

class Mensaje(models.Model):

    nombre = models.CharField(max_length=50,default="")
    mensaje = models.CharField(max_length=50,default="")


    def __str__(self):
        return self.nombre

class Item1(models.Model):

    nombre_item = models.CharField(max_length=50,default="")
    descripcion_platillo = models.CharField(max_length=50,default="")


    def __str__(self):
        return self.nombre_item