from __future__ import unicode_literals

from django.db import models
from django.core.mail import EmailMessage

from django.dispatch import receiver
from django.db.models.signals import post_save 

import re

# Create your models here.
class Participant(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	institute = models.CharField(max_length=10, default='')
	idno = models.CharField(max_length=50)
	phone = models.CharField(max_length=15, blank=True, null=True)
	can_solve = models.BooleanField(default=False)
	def __getattribute__(self, attr):
		if attr == "email":
			pattern = re.compile(r"\d{4}.{4}\d{3}P?")
			if pattern.match(str(self.idno)):
				email = "f" + self.idno[:4]+self.idno[-4:-1]+"@pilani.bits-pilani.ac.in"
				return email
			else:
				return None
		return super(Participant, self).__getattribute__(attr)
	def __str__(self):
		return self.name
		
# @receiver(post_save,sender=Participant)
def sendEmail(sender, instance, created, **kwargs):
	if created and instance.email:
		body = """
Congratulations!!!
You have registered for the world record attempt of most number of people solving Rubik's cube at the same time.
You will recieve your Rubik's Cube & Instruction manual, shortly.
Welcome aboard!

World Record Soceity
BITS Pilani
"""
		email = EmailMessage(subject="World Record Society Registration", body=body, to=[instance.email])
		email.send()