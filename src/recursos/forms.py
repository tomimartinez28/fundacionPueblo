from django import forms

from recursos.models import Recurso

class SubirRecursoForm(forms.ModelForm):
    
    class Meta:
            model = Recurso
            fields = ["nombre","descripcion", "archivo" ]
            labels = {
                'nombre' : 'Nombre',
                'descripcion' : 'Descripción del archivo',
                'archivo' : 'Seleccionar el archivo', 
            }

            widgets = {
                'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Recurso'}),
                'descripcion' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe una descripción'}),
                'archivo' : forms.FileInput(attrs={'class':'form-control', 'placeholder':'Subir'})
            }


