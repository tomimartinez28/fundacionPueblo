from tkinter import W, Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "username", "password1", "password2", "email", "telefono", "domicilio","imagen_perfil"]
        labels = {
            'first_name' : 'Nombre:',
            'last_name' : 'Apellido:',
            'username' : 'Nombre de Usuario:',
            'password1' : '',
            'password2' : '',
            'email' : 'Correo Electronico:',
            'telefono' : 'Teléfono:',
            'domicilio' : 'Domicilio:',
        }

        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placehclder':''}),
            'password1' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
            'password2' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
            'email' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
            'telefono' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
            'domicilio' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
            'imagen': 'Imagen de Perfil',
            
        }

class EditarPerfilForm(UserChangeForm):
        password = None

        class Meta:
            model = Usuario
            fields = ["first_name", "last_name", "username","email" ,"telefono", "domicilio", "imagen_perfil"]
            labels = {
                'first_name' : 'Nombre',
                'last_name' : 'Apellido',
                'username' : 'Nombre de Usuario',
                'email' : 'Correo electrónico',
                'telefono' : 'Teléfono',
                'domicilio' : 'Domicilio',
                'imagen': 'Imagen de Perfil',
            }

            widgets = {
                'imagen': forms.FileInput(attrs={'class': 'form-control'}),
                'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
                'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':''}),
                'username' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
                'email' : forms.TextInput(attrs={'class':'form-control'}),
                'telefono' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
                'domicilio' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':''}),
                
            }
        
