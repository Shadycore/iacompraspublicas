from django.urls import path, include
from django.contrib.auth import views as auth_views
from analizaproveedor.views import AnalizaProveedor

urlpatterns = [
    path('analizaproveedor', AnalizaProveedor, name='analizaproveedor'),
]