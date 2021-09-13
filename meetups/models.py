from django.db import models

# Create your models here.

class Metup(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	image = models.ImageField(upload_to='image')

	def __str__(self):
		return self.title