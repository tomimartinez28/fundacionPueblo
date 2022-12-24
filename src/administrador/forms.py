from django import forms
from eventos.models import Categoria, Modalidad

class CrearCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class CrearModalidadForm(forms.ModelForm):
    class Meta:
        model = Modalidad
        fields = ['nombre']
