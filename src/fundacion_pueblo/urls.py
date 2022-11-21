
from unicodedata import name
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path('login/', auth_views.LoginView.as_view(template_name = "login.html") , name= "login" ), #ACA HAGO USO DE LA VISTA BASADA EN UNA CLASE QUE YA TRAE DJANGO QUE SE LLAMA LoginView
    path('logout/',auth_views.logout_then_login, name= 'logout'),

    # INCLUDES (incluyo las urls de app particulares)
    path("usuarios/", include("usuarios.urls")),
    path("eventos/", include("eventos.urls")),
    path("recursos/", include("recursos.urls"))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)