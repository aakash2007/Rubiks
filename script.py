from django.core.mail import EmailMessage
from Registrations.models import *
import time, csv

def MassMail(filename):
	body = """
Hey !
Congratulations !
You have been registered for the official attempt to set a new Guinness World Record for Most Number of People solving Rubik's Cube to be held on Sunday, 16th April '17 at Gliders Club.
We will distribute the Cubes today and tomorrow i.e. the 4th and 5th April, to your rooms.

This is your opportunity to start hands-on learning and practice their solution. Please take note of the fact that The cubes that we are providing have one face colour Black instead of White. You are strictly advised to be gentle with the practicing and take care not to damage the cubes.
You can go to www.bits-wrs.ml/resources/ for tutorials.

For more information, contact-
Shivam
+91-8003322884
Abhishek
+91-9453212629
"""
	emails = []
	for line in open(filename).readlines():
		emails.append(line.strip())
	while len(emails) > 0:
		email = EmailMessage(subject="Rubik's Cube Distribution", body=body, to=["worldrecordsociety@gmail.com"], bcc=emails[:10])
		email.send()
		emails = emails[10:]
		time.sleep(1)


def  addexcel(filename):
	count = 0
	for r in csv.reader(open(filename, 'r')):
		if Participant.objects.filter(idno__iexact=r[1].strip()).count() == 0:
			p = Participant.objects.create(name=r[0].strip(), idno=r[1].strip().upper(), phone=r[2].strip(), institute="BITS")
			count += 1
	return count
