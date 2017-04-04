from django.core.mail import EmailMessage

def MassMail(filename):
	body = """
Hey !
Congratulations !
You have been registered for the official attempt to set a new Guinness World Record for the Highest Number of People to Solve the Rubik's Cube Simultaneously to be held on Sunday, 16th April '17.
We will distribute the Cubes today i.e. the 4th of April '17, at your respective Bhawans.

This is your opportunity to start hands-on learning and practice their solution. 
You are strictly advised to be gentle with the practicing and take care not to damage the cubes. 
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
		email = EmailMessage(subject="Rubik's Cube Distribution", body=body, to=["worldrecordsociety@gmail.com"], bcc=emails[:45])
		email.send()
		emails = emails[45:]