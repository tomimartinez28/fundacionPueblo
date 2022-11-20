
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponseRedirect
from core.mixins import AdminRequired
from usuarios.models import Usuario
from .forms import CrearEventoForm  
from eventos.models import Evento
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import Filtros
from django_filters.views import FilterView


# VISTA PARA ENLISTAR LOS EVENTOS EN ORDEN CRONOLOGICO
class ListaEventos(FilterView):
    template_name= "eventos/eventos.html"
    model = Evento
    context_object_name= "eventos"
    filterset_class = Filtros
    paginate_by = 5   #EL PAGINATE_BY ES PARA RENDERIZAR LA CANTIDAD DE EVENTOS :)
    def get_queryset(self):
        return Evento.objects.all().order_by("fecha")
        
    

# VISTA PARA VER UN DETALLE DEL EVENTO
class DetalleEvento(DetailView):
    model = Evento
    template_name = "eventos/detalle-evento.html"

    def get_context_data(self,*args, **kwargs):
        context = super(DetalleEvento, self).get_context_data(**kwargs)
        asiste = False
        evento = get_object_or_404(Evento, id= self.kwargs["pk"]) 
        cant_participantes = evento.cant_participantes()
        if evento.participantes.filter(id= self.request.user.id).exists():
            asiste = True
        context["asiste"] = asiste
        context["cant_participantes"] = cant_participantes
        return context



# ESTA VISTA GENERICA ME RENDERIZA UN FORMULARIO PARA CREAR EVENTOS NUEVOS
class CrearEventos(AdminRequired, LoginRequiredMixin, CreateView):
    template_name= "eventos/crear-eventos.html"
    model = Evento
    form_class = CrearEventoForm
    
    def form_valid(self, form):       # ACA LE DIGO QUE ANTES DE GUARDAR EL FORMULARIO ME CARGUE COMO ID DEL CREADOR, EL ID DEL USER LOGEADO. UN CAPO DJANGO ;)
        f = form.save(commit=False)
        f.creador_id = self.request.user.id
        return super(CrearEventos, self).form_valid(form) 

    def get_success_url(self, **kwargs):
        return reverse('eventos:lista-eventos')



#VISTA PARA MODIFICAR UN EVENTO
class ModificarEventos(AdminRequired, LoginRequiredMixin, UpdateView):
    template_name= "eventos/modificar-eventos.html"
    model = Evento
    form_class = CrearEventoForm
    def get_success_url(self, **kwargs):
        return reverse('eventos:lista-eventos')





#VISTA PARA ELIMINAR UN EVENTO
class EliminarEvento(AdminRequired,LoginRequiredMixin, DeleteView):
    template_name = "eventos/eliminar-eventos.html"
    model = Evento
    def get_success_url(self, **kwargs):
        return reverse('eventos:lista-eventos')




#VISTA PARA INSCRIBIRME A UN EVENTO

def Asistir(request, pk):
    evento = get_object_or_404(Evento, id= request.POST.get("evento_id"))
    asiste = False
    if evento.participantes.filter(id = request.user.id).exists():
        evento.participantes.remove(request.user)
        asiste = False
    else:
        evento.participantes.add(request.user)  
        asiste = True
    
    return HttpResponseRedirect(reverse('eventos:detalle', args=[str(pk)]))


# FILTRAR EVENTOS

