from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Participant(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	institute = models.CharField(max_length=10, default='')
	idno = models.CharField(max_length=50)
	phone = models.CharField(max_length=15, blank=True, null=True)
	can_solve = models.BooleanField(default=False)
	def __str__(self):
		return self.name
		