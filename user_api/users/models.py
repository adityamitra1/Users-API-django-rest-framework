from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.SmallIntegerField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	company_name = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zipcode = models.PositiveIntegerField()
	email = models.CharField(max_length=50)
	web = models.URLField()
	age = models.PositiveSmallIntegerField()

	def __str__(self):
		return ((self.first_name)+" "+(self.last_name))