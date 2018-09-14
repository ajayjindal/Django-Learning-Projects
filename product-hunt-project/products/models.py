from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
	"""docstring for product"""
	title = models.CharField(max_length=50)
	url = models.URLField()
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	body = models.TextField()

	hunter = models.ForeignKey(User,on_delete=models.CASCADE)

	def pub_date_pretty(self):
		return pub_date.strftime('%b %e %Y')

	def summary(self):
		return self.body[:100]

	def __str__(self):
		return self.title