from django.shortcuts import render, redirect, get_object_or_404
from plantilla.views import Template
from plantilla.models import TemplateModel


# Create your views here.

# Template object clone


def step1(request):
    context = {}
    savedTemplate = TemplateModel.objects.latest('id')
 
    if (request.method == 'POST'):
              
        return redirect('paso2/')
    

    context['current_step'] = 1
    context['step_text'] = 'Información básica'
    context['savedTemplate'] = savedTemplate
    return render(request, 'step1.html', context)

def step2(request):
    context = {}
    context['current_step'] = 2
    context['step_text'] = 'Personalización'
    return render(request, 'step2.html', context)