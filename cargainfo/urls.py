from django.urls import path, include
from django.contrib.auth import views as auth_views
from cargainfo.views import CargaInfoView

urlpatterns = [
    path('cargainfo', CargaInfoView, name='cargainfo'),

]