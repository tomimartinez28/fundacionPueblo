from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefono=models.CharField(max_length=255, null=True, blank=True)
    domicilio=models.CharField(max_length=255, null=True, blank=True)
    es_admin = models.BooleanField(default=False)
    imagen_perfil = models.ImageField(upload_to="imagenes_perfil", null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
