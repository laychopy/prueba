# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from app.models import *
# from app.models import Contact


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Tu nombre *', widget=forms.TextInput(attrs={'placeholder': 'ej: Luis Albarenga'}))

    correo = forms.EmailField(label='Tu correo electronico *', widget=forms.TextInput(attrs={'placeholder': 'ej: alguien@mail.com'}))

    sitio_web = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'ej: http://tusitio.com'}))

    mensaje = forms.CharField(label='Su mensaje *', widget=forms.Textarea)

TIPOS = [('', '--selectiona un tipo--')] + [(t.id, t.tipo) for t in Categoria.objects.all()]
ALTURA = [('', '--altura--')]
ANCHO = [('', '--ancho--')]
ARO = [('', '--aro--')]


class BuscarForm(forms.Form):
    tipos = forms.ChoiceField(label="Tipo de vehiculo", widget=forms.Select(),
                              choices=(TIPOS))
    aro = forms.ChoiceField(label="Tipo de vehiculo", widget=forms.Select(),
                            choices=(TIPOS))
    altura = forms.ChoiceField(label="Altura", widget=forms.Select(),
                               choices=(ALTURA))
    ancho = forms.ChoiceField(label="Ancho", widget=forms.Select(),
                              choices=(ANCHO))
    aro = forms.ChoiceField(label="Aro", widget=forms.Select(),
                            choices=(ARO))
