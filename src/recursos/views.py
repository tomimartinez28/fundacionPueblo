from dataclasses import field
import http
import os
from django.shortcuts import render

from django.http import HttpResponse, Http404

import fundacion_pueblo
from .models import Recurso

import os
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import AdminRequired
from django.views.generic import CreateView, ListView, DeleteView
from .forms import SubirRecursoForm
from django.urls import reverse
"""
def subir_archivo(request):
    ctx = {
        'form' : form
    }
    if request.method == 'POST':
        form = SubirRecursoForm(request.POST, request.FILES )
        archivo = request.FILES['archivo'] # donde archivo es el nombre del campo en el form
        recurso = Recurso.objects.create(archivo = archivo)
        recurso.save()
        return HttpResponse("Subiste el archivo " + str(archivo))
    else:
        form = SubirRecursoForm()
    return render(request, 'recursos/subir.html', ctx)

"""

class SubirRecursos(AdminRequired, LoginRequiredMixin, CreateView):
    template_name= "recursos/subir-recursos.html"
    model = Recurso
    form_class = SubirRecursoForm
    
    def form_valid(self, form):       # ACA LE DIGO QUE ANTES DE GUARDAR EL FORMULARIO ME CARGUE COMO ID DEL CREADOR, EL ID DEL USER LOGEADO. UN CAPO DJANGO ;)
        f = form.save(commit=False)
        f.creador_id = self.request.user.id
        return super(SubirRecursos, self).form_valid(form) 

    def get_success_url(self, **kwargs):
        return reverse('recursos:recursos')


class ListaRecursos(ListView):
    template_name= "recursos/recursos.html"
    model = Recurso
    context_object_name= "recursos"
    def get_queryset(self):
            return Recurso.objects.all().order_by("created")
            

class EliminarRecursoView(AdminRequired,LoginRequiredMixin, DeleteView):
    template_name = "recursos/eliminar-recurso.html"
    model = Recurso
    def get_success_url(self, **kwargs):
        return reverse('recursos:recursos')
