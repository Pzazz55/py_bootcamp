'''
**********************************************************************************************************
Working with Emails in Python - Lesson 134 to 136
**********************************************************************************************************
The below script demonstrates :-
- how to send emails
- how to check out the inbox for received messages.
**********************************************************************************************************
- Note, this process is highly reliant on admin privileges on both local computer, internet provider, 
  and email provider.
- Steps involved are: connect to email server, confirming connection, setting a protocol, logging on,
  and sending the message.
- use the built-in smtplib library
- each major email provider has their own SMTP Server (Simple Mail Transfer Protocol)
- for Gmail Users, they need to generate an app password instead of the normal password - to let the Gmail
  know that the Python script is attempting to access the account.
**********************************************************************************************************
'''

import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587) #using port 587 uses TLS encryption

smtp_object.ehlo() #connection - to bring the server
print(smtp_object.ehlo()) #prints starting with 250, to show a successfull connection

smtp_object.starttls()

#login to Gmail and enable 2-Step Verification - password & phone number
#go to Securities Page in Gmail, and setup App Password
#Gmail Passkey: tnqh hcde ziaq jrtb

email = input("Enter the Email Address ::") #give the Gmail Address
# password = 'tnqh hcde ziaq jrtb'
password = getpass.getpass("Enter the Email Password ::") #give the above generated App Password
smtp_object.login(email, password)

#sending an email
from_address = email
to_address = email #email being to self
subject = input("Enter the subject line ::")
body = input("Enter the body message ::")
msg = "Subject: "+subject+'\n'+body

smtp_object.sendmail(from_address, to_address, msg) 
#if an empty dictionary is returned, the sending was successfully.

smtp_object.quit()