from turtle import title
from typing_extensions import Required
from django import forms


class createnewtask(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=100)
    description= forms.CharField(label="descripcion de la tarea", widget=forms.Textarea)