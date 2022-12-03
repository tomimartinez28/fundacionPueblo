from django.urls import path
from . import views

app_name = "administrador"

urlpatterns = [
    path('settings', views.Administrador.as_view(), name = "administrador"), 
    path('eliminar-categoria/<int:pk>', views.EliminarCategoria.as_view(), name = 'eliminar-categoria'),
    path('crear-categoria', views.CrearCategoria.as_view(), name = 'crear-categoria')
    
]    