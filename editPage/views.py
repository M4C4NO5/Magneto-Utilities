from django.shortcuts import render, redirect

# Create your views here.

def step1(request):
    if (request.method == 'POST'):
        return redirect('paso2/')

    return render(request, 'step1.html')

def step2(request):
    return render(request, 'step2.html')