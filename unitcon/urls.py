"""Aqui esta conectado el url del homepage"""

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
]