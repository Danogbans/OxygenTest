from django.db import models

# Aqui es para crear los modelos para el base de datos

class UnitConverter(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100, blank=True)
	description = models.TextField(max_length=100, blank=True)
	created = models.DateTimeField(auto_now_add=True)
