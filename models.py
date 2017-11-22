#coding: utf-8
from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=100, verbose_name = 'Prénom')
	target = models.CharField(max_length=100,)
	password = models.CharField(max_length=100, verbose_name = 'Mot de passe',)
	def __str__(self):
		return self.name

