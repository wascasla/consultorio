from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView
from .forms import *

def turno_new(request):
	if request.method == "POST":
		form = TurnoForm(request.POST)
		if form.is_valid():
			turno = form.save()
			return redirect('gturnos.views.viewTurno.turno_detail',pk=turno.pk)
	else:		
		form = TurnoForm()
		return render(request, 'gturnos/turno/new.html', {'form':form})