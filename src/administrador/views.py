from django.views.generic import ListView, DeleteView, CreateView
from eventos.models import Evento, Categoria, Modalidad
from django.urls import reverse
from .forms import CrearCategoriaForm
from . import forms
# Create your views here.

#LISTA LOS EVENTOS EN LA SECCION DE ADMINISTRADOR
class Administrador(ListView):
    template_name= "administrador/administrador.html"
    model = Evento
    context_object_name= "eventos"

    def get_queryset(self):
        return Evento.objects.all().order_by("nombre")


    def get_context_data(self, **kwargs):
        context = super(Administrador, self).get_context_data(**kwargs)
        context.update({
            'categorias': Categoria.objects.order_by('nombre'),
            'modalidad': Modalidad.objects.order_by('nombre')
        })
        return context



# CREAR CATEGORIAS
class CrearCategoria(CreateView):
    template_name: str = "administrador/crear-categoria.html"
    model = Categoria
    form_class = CrearCategoriaForm 
    def get_success_url(self, **kwargs):
        return reverse('administrador:administrador')

# ELIMINAR CATEGORIAS

class EliminarCategoria(DeleteView):
    template_name = "administrador/eliminar-categoria.html"
    model = Categoria
    def get_success_url(self, **kwargs):
        return reverse('administrador:administrador')


