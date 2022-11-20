from django.contrib import admin

from fundacion_pueblo.views import eventos
from .models import Evento, Categoria, Modalidad
# Register your models here.


class eventosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated', "creador") #Aca le digo que estos sean campos de solo lectura ;) 

admin.site.register(Evento, eventosAdmin)

admin.site.register(Categoria)
admin.site.register(Modalidad)

