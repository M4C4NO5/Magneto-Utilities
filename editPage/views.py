from django.shortcuts import render, redirect, get_object_or_404
from plantilla.views import Template
from plantilla.models import TemplateModel


# Create your views here.

# Template object clone


def step1(request):
    if not TemplateModel.objects.exists():
        basis = TemplateModel(name="prueba",title="prueba",desc="prueba",color="prueba",url="prueba")
        basis.save()
    if TemplateModel.objects.exists():
        context = {}
        savedTemplate = TemplateModel.objects.latest('id')
        default_name = savedTemplate.name
        default_title = savedTemplate.title
        default_desc = savedTemplate.desc
        default_color = savedTemplate.color
        default_url = savedTemplate.url

    baseTemplate = Template(default_name,default_title,default_desc,default_url,default_color)

    editableTemplate = baseTemplate.clone()
    if (request.method == 'POST'):
        context["title"]=request.POST["title"]
        context["desc"]=request.POST["desc"]
        context["url"]=request.POST["url"]

        title = context["title"]
        desc = context["desc"]
        url = context["url"]
        
        editableTemplate.title = title
        editableTemplate.desc = desc
        editableTemplate.url = url

        return redirect('paso2/')


    context['current_step'] = 1
    context['step_text'] = 'Información básica'
    context['savedTemplate'] = savedTemplate
    return render(request, 'step1.html', context)

def step2(request):
    context = {}
    context['current_step'] = 2
    context['step_text'] = 'Personalización'

    #Getting data from step 1
    if 'title' in request.POST:
        context['title']= request.POST.get('title','')
        prueba = context['title']
        print(prueba)
    if 'desc' in request.POST:
        context['desc']= request.POST.get('desc','')
    if 'url' in request.POST:
        context['url']= request.POST.get('url','')
    return render(request, 'step2.html', context)