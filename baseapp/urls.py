from django.urls import path, include
from django.contrib.auth import views as auth_views
from baseapp.views import Home
from analizaproveedor.views import AnalizaProveedor
from buscapatrones.views import BuscaPatrones

urlpatterns = [
    path('', Home, name='home'),
    path('/analizaproveedor', AnalizaProveedor, name='analizaproveedor'),
    path('/buscapatrones', BuscaPatrones, name='buscapatrones'),

]