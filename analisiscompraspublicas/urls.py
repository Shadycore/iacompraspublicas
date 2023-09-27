from django.urls import path, include
from analisiscompraspublicas.views import contratosView, compradoresView, compradores2View, \
                                        proveedoresView, analisisvariosView, tendencia_contratos, \
                                        grafico_arima, tendencia_valor_contrato
                                        

urlpatterns = [
    path('contratos', contratosView, name="contratosView"),
    path('compradores', compradoresView, name="compradoresView"),
    path('compradores2', compradores2View, name="compradores2View"),
    path('proveedores', proveedoresView, name="proveedoresView"),
    path('analisisvarios', analisisvariosView, name="analisisvariosView"),



    path('aivarios/', tendencia_contratos, name="tendencia_contratos"),
    path('aivarios2/', grafico_arima, name="grafico_arima"),
    path('aivarios3/', tendencia_valor_contrato, name="tendencia_valor_contrato"),


]
