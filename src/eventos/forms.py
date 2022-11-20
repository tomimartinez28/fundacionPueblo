from cProfile import label
from dataclasses import fields
from tkinter import Widget
from unicodedata import category
from django import forms
from .models import Evento

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class CrearEventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["nombre", "fecha", "hora", "lugar", "categoria", "modalidad", "descripcion", "imagen"]
        labels = {
            'nombre' : 'Nombre',
            'fecha' : 'Fecha',
            'hora' : 'Hora',
            'lugar' : 'Lugar',
            'categoria' : 'Categoría',
            'modalidad' : 'Modalidad',
            'descripcion' : 'Descripción',
            

        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Evento'}),
            'fecha' : DateInput(),
            'hora' : TimeInput(),
            'lugar' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Lugar'}),
            'categoria' : forms.Select(attrs={'class':'form-select',  'placeholder':'Categoría'}),
            'modalidad' : forms.Select(attrs={'class':'form-select', 'placeholder':'Modalidad'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe una descripción'})
        }


