from django.shortcuts import render
from django.views.generic import TemplateView

def inicio(request):
    template_name = "index.html"
    ctx = {

    }
    return render(request, template_name, ctx )


def eventos(request):
    return render(request, "eventos.html", {})


