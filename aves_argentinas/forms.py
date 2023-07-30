from django import forms
from aves_argentinas.models import Aves

    
class AveFormulario(forms.Form):
    orden = forms.CharField(required=True, max_length=200)
    familia = forms.CharField(required=True, max_length=200)
    especie = forms.CharField(required=True, max_length=200)
    nombre = forms.CharField(required=True, max_length=200)
    caracteristicas = forms.CharField(widget=forms.Textarea)
    ultima_observacion = forms.DateField()
    #foto = forms.ImageField()
    
class FaunaFormulario(forms.Form):
    orden = forms.CharField(required=True, max_length=200)
    familia = forms.CharField(required=True, max_length=200)
    especie = forms.CharField(required=True, max_length=200)
    nombre = forms.CharField(required=True, max_length=200)
    caracteristicas = forms.CharField(widget=forms.Textarea)
    ultima_observacion = forms.DateField()
    
class FloraFormulario(forms.Form):
    especie = forms.CharField(required=True, max_length=200)
    nombre = forms.CharField(required=True, max_length=200)
    tipo = forms.CharField(max_length=200)
    caracteristicas = forms.CharField(widget=forms.Textarea)  