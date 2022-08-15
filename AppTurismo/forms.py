from django import forms
from django.db import models
from django.forms import widgets
from .models import ZonaTuristica, UsuarioCliente
from django.contrib.auth.forms import UserCreationForm

class ZonaTuristicaForm(forms.ModelForm):
    class Meta:
        model = ZonaTuristica
        fields = [
            'nombre',
            'descripcion',
            'distrito',
            'estructura',
            'horario',
            'year',
            'disponible',
            'img',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'Ingrese nombre del sitio'}),
            'descripcion': forms.Textarea(attrs={'placeholder':'¿Como es el sitio?'}),
            'horario': forms.TextInput(attrs={'placeholder':'hh:mm:ss'}),
            'year': forms.TextInput(attrs={'placeholder':'Ingrese año'}),
            
        }

    def clean_nombre(self,*args,**kwargs):
        name = self.cleaned_data.get('nombre')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('La primera letra de cada palabra va con mayuscula')

class RegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioCliente
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'image',
        ]

        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Ingrese su usuario'}),
            'first_name': forms.TextInput(attrs={'placeholder':'Ingrese sus nombres'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Ingrese sus apellidos'}),
            'email': forms.EmailInput(attrs={'placeholder':'Ingrese su correo'}),
            
        }


