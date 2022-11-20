from dataclasses import field
from tkinter import Widget
import django_filters
from .models import Evento
from .forms import DateInput


class Filtros(django_filters.FilterSet):
   
    fecha = django_filters.DateFromToRangeFilter(widget= django_filters.widgets.RangeWidget(attrs={'type':'date'}))

    class Meta:
        model = Evento
        
        fields = {
            "nombre" : ['icontains'],
            "categoria" :[ 'exact'],
            "fecha" : ['exact']}

