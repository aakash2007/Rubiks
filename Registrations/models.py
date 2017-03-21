from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Participant(models.Model):
	GENDERS = (('M', 'Male'), ('F', 'Female'))
	name = models.CharField(max_length=50, null=False, blank=False)
	gender = models.CharField(max_length=10, null=False, blank=False)
	idno = models.CharField(max_length=15)
	phone = models.CharField(max_length=15)
	email = models.CharField(max_length=50)
	def __str__(self):
		return self.name
		