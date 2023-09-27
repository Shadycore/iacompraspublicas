from django.urls import path, include
from analisiscompraspublicas.views import contratosView, compradoresView, compradores2View, proveedoresView, analisisvariosView, tendencia_contratos

urlpatterns = [
    path('contratos', contratosView, name="contratosView"),
    path('compradores', compradoresView, name="compradoresView"),
    path('compradores2', compradores2View, name="compradores2View"),
    path('proveedores', proveedoresView, name="proveedoresView"),
    path('analisisvarios', analisisvariosView, name="analisisvariosView"),



    path('aivarios/', tendencia_contratos, name="tendencia_contratos"),

]
