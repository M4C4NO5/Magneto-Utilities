from django.shortcuts import render
import copy

# Create your views here.

def plantilla(request):

    return render(request, 'plantilla.html')

class Template:
    def __init__(name, title, url,font, font_size, color, description,self):
        self.name = name
        self.title = title
        self.url = url
        self.desc = description
        self.font = font
        self.font_size = font_size
        self.color = color
    
    
    def clone(self):
        return copy.deepcopy(self)



