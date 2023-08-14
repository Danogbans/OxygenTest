"""Aqui esta conectado el url de la aplicacion (unitcon)"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unitcon.urls')),
]
