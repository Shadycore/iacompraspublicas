from django.urls import path, include
from django.contrib.auth import views as auth_views
from buscapatrones.views import BuscaPatrones

urlpatterns = [
    path('/buscapatrones', BuscaPatrones, name='buscapatrones'),
    
]