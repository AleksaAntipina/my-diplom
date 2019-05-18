from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	company_name = models.CharField(max_length=15)
	company_description = models.CharField(max_length=500)
	working_position = models.CharField(max_length=15)
	country = models.CharField(max_length=15)
	e_mail = models.EmailField(max_length=60)
	linked_in_reference = models.URLField(max_length=100)
    
	def publish(self):
		self.first_name = 'test'
		self.save()

	def __str__(self):
		return self.last_name