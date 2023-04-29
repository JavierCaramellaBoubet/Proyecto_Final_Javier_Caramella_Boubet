from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludar(request):
    return HttpResponse("Hola Mundo!")


def probandoHtml(request):
    archivo= open(r"C:\ProyectoFinal\Plantillas\template.html")

    template=Template(archivo.read())
    archivo.close()
    
    contexto=Context()
    documento=template.render(contexto)
    return HttpResponse(documento)





