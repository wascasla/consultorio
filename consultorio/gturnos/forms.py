from django import forms
from .models import *
from django.forms import  TextInput
from datetimewidget.widgets import DateTimeWidget, DateWidget 

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
		fields = ('fecha','medico','paciente','organizacion')
		widgets = {
		'fecha': DateWidget(attrs={'id':"fecha"}, bootstrap_version=3),
		'medico': TextInput(attrs={'class':'form-control'}),
		'paciente': TextInput(attrs={'class':'form-control'}),
		'organizacion': TextInput(attrs={'class':'form-control'})	
		#'fecha': TextInput(attrs={'class':'input-group date'})
		
		}
		#fecha = forms.DateField(widget=forms.SelectDateWidget())
		