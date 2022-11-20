
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from datetime  import datetime, time
from usuarios.models import Usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

        
class Modalidad(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre



class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null= True, blank= True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(null= True)
    lugar = models.CharField(max_length=255, null= True)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.SET_NULL, null= True, blank= True)
    created  = models.DateTimeField(auto_now_add=True, blank= True) #cuando se creo fecha el evento
    updated  =models.DateTimeField(auto_now_add=True, blank= True)  #cuando se elimino fecha
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_eventos", null=True)
    descripcion = models.TextField(null=True, blank=True)
    participantes = models.ManyToManyField(Usuario, related_name = "participantes", blank=True)
    imagen = models.ImageField(upload_to="imagen_eventos", null=True, blank=True)



    def cant_participantes(self):
        return self.participantes.count()
    
    def __str__(self):
        return self.nombre


