from django.shortcuts import render

# Create your views here.

def AnalizaProveedor(request):
    template_name = "analizaproveedor.html"
    return render(request, template_name)
