from django.urls import path
from . import views

app_name = "administrador"

urlpatterns = [
    path('settings', views.Administrador.as_view(), name = "administrador"), 
    path('eliminar-categoria/<int:pk>', views.EliminarCategoria.as_view(), name = 'eliminar-categoria'),
    path('crear-categoria', views.CrearCategoria.as_view(), name = 'crear-categoria'),
    path('eliminar-modalidad/<int:pk>', views.EliminarModalidad.as_view(), name = 'eliminar-modalidad'),
    path('crear-modalidad', views.CrearModalidad.as_view(), name = 'crear-modalidad')
    
]    