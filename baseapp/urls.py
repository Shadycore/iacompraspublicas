from django.urls import path, include
from django.contrib.auth import views as auth_views
from baseapp.views import Home


urlpatterns = [
    path('', Home, name='home'),

]