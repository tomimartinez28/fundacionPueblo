from django.contrib import admin

from recursos.models import Recurso

# Register your models here.
class recursosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Recurso, recursosAdmin )