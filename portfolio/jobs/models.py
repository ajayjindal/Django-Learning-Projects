from django.db import models

# Create your models here.
class Job(models.Model):
	"""docstring for Jobs"""
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=50,default='test')
	summary = models.CharField(max_length=200)
		