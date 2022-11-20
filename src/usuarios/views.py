
from django.views.generic.edit import CreateView, UpdateView
from .forms import FormularioRegistro, EditarPerfilForm
from .models import Usuario
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# ESTA VIEW VA A RENDERIZAR EL FORMULARIO PARA QUE SE REGISTREN LOS USUARIOS :)

class Registro(CreateView):
    model = Usuario
    form_class = FormularioRegistro
    template_name = "usuarios/registrarse.html"

    def get_success_url(self, **kwargs):
        return reverse("inicio") 

class EditarPerfil(UpdateView):
    model = Usuario
    form_class = EditarPerfilForm
    template_name = "usuarios/editar-perfil.html"

    def get_success_url(self, **kwargs):
        return reverse("inicio") 

def miperfil(request):
    template_name = "usuarios/mi-perfil.html"
    ctx = {

    }
    return render(request, template_name, ctx )


class CambiarContraseñaView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'usuarios/cambiar-contraseña.html'
    def get_success_url(self, **kwargs):
        return reverse("inicio")