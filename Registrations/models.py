from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Participant(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	idno = models.CharField(max_length=50)
	phone = models.CharField(max_length=15, blank=True, null=True)
	email = models.CharField(max_length=50, blank=True, null=True)
	def __str__(self):
		return self.name
		