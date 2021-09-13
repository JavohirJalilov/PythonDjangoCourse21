# from typing_extensions import TypeGuard
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class Location(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.name} {self.address}"

class Metup(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	image = models.ImageField(upload_to='image')
	location = models.ForeignKey(Location,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title