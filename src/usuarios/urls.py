from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "usuarios"

urlpatterns = [
    path("registrarse/", views.Registro.as_view(), name = "registro"),
    path("mi-perfil/", views.miperfil, name= "mi-perfil"),
    path("editar-perfil/<int:pk>", views.EditarPerfil.as_view(), name = "editar-perfil"),
    path('cambiar-contraseña/', views.CambiarContraseñaView.as_view(), name= "cambiar-contraseña")

    #path('cambiar-contraseña/', auth_views.PasswordChangeView.as_view(template_name= 'usuarios/cambiar-contraseña.html'), name= 'cambiar-contraseña')
]