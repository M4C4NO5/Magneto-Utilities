from django.shortcuts import render, redirect

# Create your views here.

def step1(request):
    context = {}
    if (request.method == 'POST'):
        
        return redirect('paso2/')
    context['current_step'] = 1
    context['step_text'] = 'Información básica'
    return render(request, 'step1.html', context)

def step2(request):
    context = {}
    context['current_step'] = 2
    context['step_text'] = 'Personalización'
    return render(request, 'step2.html', context)