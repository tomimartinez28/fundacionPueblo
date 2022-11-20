from django.db import models
from datetime  import datetime, time
from usuarios.models import Usuario


# Create your models here.

class Recurso(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to = "archivos")
    created  = models.DateTimeField(auto_now_add=True, blank= True) #cuando se creo fecha el evento
    updated  =models.DateTimeField(auto_now_add=True, blank= True)  #cuando se elimino fecha
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_recursos")
    descripcion = models.TextField(null=True, blank=True)
   

    def __str__(self):
        return self.nombre 