from django.urls import path
from . import views

app_name = "eventos"

urlpatterns = [
    path("lista-eventos/", views.ListaEventos.as_view(), name = "lista-eventos"), 
    path("crear-eventos/", views.CrearEventos.as_view(), name = "crear-eventos"),
    path("modificar-eventos/<int:pk>/", views.ModificarEventos.as_view(), name="modificar-eventos"),
    path("eliminar-eventos/<int:pk>/", views.EliminarEvento.as_view(), name= "eliminar-eventos"),
    path("detalle/<int:pk>/", views.DetalleEvento.as_view(), name = "detalle"),
    path("asistir/<int:pk>", views.Asistir, name = "asistir"),
    
]    