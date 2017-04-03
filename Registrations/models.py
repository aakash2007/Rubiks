from __future__ import unicode_literals

from django.db import models
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
import re
# Create your models here.
def validate_idno(idno):
	pattern = re.compile(r"(\d{4}).{4}(\d{3})P")
	match = pattern.match(str(idno))
	if not match:
		raise ValidationError("Enter A Valid ID No.")

class Participant(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	institute = models.CharField(max_length=10, default='')
	idno = models.CharField(max_length=50)
	phone = models.CharField(max_length=15, blank=True, null=True)
	can_solve = models.BooleanField(default=False)
	def save(self, *args, **kwargs):
		match = re.compile(r"(\d{4}).{4}(\d{3})P?").match(self.idno)
		if match:
			try:
				bitsian = BITSians.objects.filter(idno__istartswith=match.group(1)).filter(idno__endswith=match.group(2)+'P')[0]
				bitsian.registered = True
				bitsian.save()
				self.idno = bitsian.idno
			except:
				pass
		return super(Participant,self).save(*args, **kwargs)
	def __getattribute__(self, attr):
		if attr == "email":
			try:
				return BITSians.objects.get(idno=self.idno).email
			except:
				return None
		return super(Participant, self).__getattribute__(attr)
	def __str__(self):
		return self.name


class BITSians(models.Model):
	idno = models.CharField(max_length=12, validators=[validate_idno], primary_key=True)
	name = models.CharField(max_length=100, blank=False)
	hostel = models.CharField(max_length=4, blank=False)
	room = models.PositiveSmallIntegerField()
	email = models.EmailField(blank=False)
	registered = models.BooleanField(default=False)
	def __unicode__(self):
		return self.idno
	class Meta:
		verbose_name = 'BITSian'
		verbose_name_plural = 'BITSians'
		ordering = ('idno',)