from django.shortcuts import render

def inicio(request):
    template_name = "index.html"
    ctx = {

    }
    return render(request, template_name, ctx )




