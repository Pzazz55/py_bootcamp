'''
Sending Emails using Python.

To send emails with Python, we need to manually go through the steps of connecting to an
email server, confirming connection, setting a protocol, logging on and sending the message.
The built-in smtplib library in python makes these steps simple function calls.
Each major email provider (Gmail, Yahoo, Outlook, Hotmail, AT&T, Verizon, Comcast) have their
own SMTP (Simple Mail Transfer Protocol) Server.
For Gmail user, we need to generate an App Password instead of a Normal/Regular Password.
This let's Gmail know that the Python Script attempting to access your account is authorized
by you.
'''
import getpass
import smtplib


smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.startls()

pwd = getpass.getpass("Enter the Password: ")

