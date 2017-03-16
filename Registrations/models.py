from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Participant(models.Model):
	GENDERS = (('M', 'Male'), ('F', 'Female'))
	name = models.CharField(max_length=100, null=False, blank=False)
	gender = models.CharField(max_length=1, choices=GENDERS, null=False, blank=False)
	phone = models.BigIntegerField(null=False, blank=False)
	email = models.EmailField(unique=True, blank=False, null=False)
	def __str__(self):
		return self.name
		