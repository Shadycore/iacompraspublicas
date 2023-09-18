from django.shortcuts import render

# Create your views here.

#vista de home
def Home(request):
    template_name = 'baseapp/home.html'
    return render(request, template_name)

