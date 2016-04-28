from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *

def index(request):
	return render(request,'gturnos/plantilla-dash.html', {})

def organizacion_new(request):
	if request.method == "POST":
		form = OrganizacionForm(request.POST)
		if form.is_valid():
			oganizacion = form.save()
			return redirect('gturnos.views.organizacion_detail',pk=oganizacion.pk)
	else:		
		form = OrganizacionForm()
		return render(request, 'gturnos/organizacion/new.html', {'form':form})


def organizacion_edit(request, pk):
	organizacion = get_object_or_404(Organizacion, pk=pk)
	if request.method == "POST":
		form = OrganizacionForm(request.POST, instance=organizacion)
		if form.is_valid():			
			organizacion = form.save()
			return redirect('gturnos.views.organizacion_detail',pk=organizacion.pk)
	else:		
		form = OrganizacionForm(instance=organizacion)
		return render(request, 'gturnos/organizacion/edit.html', {'form':form})


def organizacion_detail(request, pk):
	org = get_object_or_404(Organizacion, pk=pk)	
	return render(request, 'gturnos/organizacion/detail.html', {'org':org})


def organizacion_all(request):
	orgTodas = Organizacion.objects.all()
	return render(request, 'gturnos/organizacion/orgList.html', {'orgTodas':orgTodas})
