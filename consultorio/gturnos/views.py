from django.shortcuts import render,render_to_response
from django.views.generic.base import TemplateView

def index(request):
	return render(request,'gturnos/hola.html', {})