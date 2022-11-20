
from django.urls import path
from django.conf.urls.static import static


from django.conf import settings
from . import views


app_name = "recursos"

urlpatterns = [
    path("lista-recursos/", views.ListaRecursos.as_view(), name= "recursos"),
    path("subir-recursos/", views.SubirRecursos.as_view(), name= "subir-recursos" ),
    path("eliminar-recurso/<int:pk>/", views.EliminarRecursoView.as_view(), name= "eliminar-recurso")
]