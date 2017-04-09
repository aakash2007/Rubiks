from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from Registrations.models import *
import time, csv

def MassMail(filename):
	body = render_to_string('mail.html')
	emails = []
	errlog = csv.writer(open('/home/ubuntu/mail_error.log', 'a'))
	for line in open(filename).readlines():
		emails.append(line.strip().lower())
	emails = list(set(emails))
	while len(emails) > 0:
		email = EmailMultiAlternatives(subject="Rubik's Cube Workshop", body="...", to=["worldrecordsociety@gmail.com"], bcc=emails[:10])
		email.attach_alternative(body, "text/html")
		try:
			email.send()
		except:
			for em in emails[:10]:
				errlog.writerow([em])
		emails = emails[10:]
		time.sleep(1)

def  addexcel(filename):
	count = 0
	for r in csv.reader(open(filename, 'r')):
		if Participant.objects.filter(idno__iexact=r[1].strip()).count() == 0:
			p = Participant.objects.create(name=r[0].strip(), idno=r[1].strip().upper(), phone=r[2].strip(), institute="BITS")
			count += 1
	return count
