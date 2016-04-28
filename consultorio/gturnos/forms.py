from django import forms
from .models import *
from django.forms import  TextInput

class OrganizacionForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Organizacion
		fields = ('nombre','domicilio','telefono')
		widgets = {
		'nombre': TextInput(attrs={'class':'form-control'}),
		'domicilio': TextInput(attrs={'class':'form-control'}),
		'telefono': TextInput(attrs={'class':'form-control'}),
		}


class TurnoForm(forms.ModelForm):
	"""docstring for OrganizacionForm"""
	class Meta:
		model = Turno
		fields = ('medico','paciente','organizacion','fecha')
		widgets = {
		'medico': TextInput(attrs={'class':'form-control'}),
		'paciente': TextInput(attrs={'class':'form-control'}),
		'organizacion': TextInput(attrs={'class':'form-control'}),
		'fecha': TextInput(attrs={'class':'form-control'}),
		}
		