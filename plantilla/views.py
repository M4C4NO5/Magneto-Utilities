from django.shortcuts import render
import copy

# Create your views here.

def plantilla(request):

    return render(request, 'plantilla.html')

class Template:
    def __init__(self, name, title,description, url, color, font, font_color):
        self.name = name
        self.title = title
        self.desc = description
        self.url = url
        self.color = color
        self.font = font
        self.font_color = font_color


    def clone(self):
        return copy.deepcopy(self)



