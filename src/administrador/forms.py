from django import forms
from eventos.models import Categoria

class CrearCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


