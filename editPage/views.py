from django.shortcuts import render, redirect, get_object_or_404
from plantilla.views import Template
from plantilla.models import TemplateModel


# Create your views here.

# Template object clone


def template_to_edit(request):
   
    if TemplateModel.objects.exists():
        savedTemplate = TemplateModel.objects.latest('id')
        default_name = savedTemplate.name
        default_title = savedTemplate.title
        default_desc = savedTemplate.desc
        if 'color' in request.session:
            default_color = request.session['color']
        else:
            default_color = savedTemplate.color
        default_url = savedTemplate.url
        if 'font' in request.session:
            default_font = request.session['font']
        else:
            default_font = savedTemplate.font
        if 'font_color' in request.session:
            default_font_color = request.session['font_color']
        else:
            default_font_color = savedTemplate.font_color

    baseTemplate = Template(default_name,default_title,default_desc,default_url,default_color, default_font, default_font_color)
    return baseTemplate.clone()
    
def step1(request):
    context = {}
    if 'font' in request.session:
        del request.session['font']
    if 'font_color' in request.session:
        del request.session['font_color']
    if 'color' in request.session:
        del request.session['color']
    template = template_to_edit(request)
    context['template'] = template 

    if (request.method == 'POST'):
        title=request.POST["title"]
        desc =request.POST["desc"]
        url =request.POST["url"]
        return redirect(f'paso2/?title={title}&desc={desc}&url={url}')


    context['current_step'] = 1
    context['step_text'] = 'Información básica'
    context['template'] = template
    return render(request, 'step1.html', context)

def step2(request):
    template = template_to_edit(request)
    context = {}
    context['current_step'] = 2
    context['step_text'] = 'Personalización'
    title = request.GET.get('title', '')
    desc = request.GET.get('desc', '')
    url = request.GET.get('url', '')
    template.title = title
    template.desc = desc
    template.url = url

    

    if request.method == 'POST':
        if 'change-font' in request.POST:

            font = request.POST['change-font']
  
            template.font = font
            context['template'] = template
            request.session['font'] = font
            return render(request, 'step2.html', context)
        if 'change-font-color' in request.POST:

            font_color = request.POST['change-font-color']
            template.font_color = font_color
            context['template'] = template
            request.session['font_color'] = font_color
            return render(request, 'step2.html', context)
        
        if 'change-color' in request.POST:
            color = request.POST['change-color']
            template.color = color
            context['template'] = template
            request.session['color'] = color
            return render(request, 'step2.html', context)
        
        if 'next-step' in request.POST:
            pass

    context['template'] = template
    return render(request, 'step2.html', context)
