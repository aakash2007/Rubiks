from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Seats(models.Model):
	seat_no = models.CharField(max_length=4, unique=True)
	def __str__(self):
		return self.seat_no
	class Meta:
		verbose_name_plural='Seats'