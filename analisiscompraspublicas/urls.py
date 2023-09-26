from django.urls import path, include
from analisiscompraspublicas.views import contratosView, compradoresView

urlpatterns = [
    path('contratos', contratosView, name="contratosView"),
    path('compradores', compradoresView, name="compradoresView"),
]
