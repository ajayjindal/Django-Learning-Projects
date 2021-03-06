from django.db import models

# Create your models here.
class Blog(models.Model):
	"""docstring for blog"""
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title