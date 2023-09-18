from django.shortcuts import render

# Create your views here.


def BuscaPatrones(request):
    template_name = "buscapatrones.html"
    return render(request, template_name)