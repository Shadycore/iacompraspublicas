from django.urls import path, include
from analisiscompraspublicas.views import contratosView, compradoresView, compradores2View

urlpatterns = [
    path('contratos', contratosView, name="contratosView"),
    path('compradores', compradoresView, name="compradoresView"),
    path('compradores2', compradores2View, name="compradores2View"),
]
