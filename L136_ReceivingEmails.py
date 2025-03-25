'''
**********************************************************************************************************
Working with Emails in Python - Lesson 134 to 136
**********************************************************************************************************
The below script demonstrates :-
- how to send emails
- how to check out the inbox for received messages.
**********************************************************************************************************
- to view the received emails with Python, we can use built in imaplib and email libraries
- imaplib library has a special syntax for searchign the inbox.
- KEYWORDS: ALL, BEFORE date, ON date, SINCE date, FROM some_string, TO some_string, CC some_string 
  and/or BCC some_string, SUBJECT string, BODY string, TEXT string with spaces, SEEN, UNSEEN, ANSWERED, 
  UNANSWERED, DELETED, UNDELETED
**********************************************************************************************************
'''

import imaplib
import getpass
import email #the built-in email library to help parse the email string (grab the actual message from the string)

M = imaplib.IMAP4_SSL('imap.gmail.com') #make a connecton to the Gmail Server

emailid_userinput = input("Enter the Email Address ::")
password = 'tnqh hcde ziaq jrtb'
# password = getpass.getpass("Enter the Email Password ::")
M.login(emailid_userinput, password)

print(M.list()) #to check everything in the emailbox
M.select('inbox') #selecting the Inbox
typ, data = M.search(None, 'SUBJECT "Test Email"') #tuple unpacking - this returns a tuple 
print(typ, data) #returns the Unique ID of email messages that match the criteria

# message_id = data[0]

#ensure that we have message IDs from the search result
if data[0]:
    message_ids = data[0].split()  #convert to a list of message IDs
    message_id = message_ids[0]  #fetching the first item of the message list
    
    #fetching the email data (RFC822)
    result, message_content = M.fetch(message_id, '(RFC822)')
    print(result, message_content)  #processing and printing the message_content
    
else:
    print("No messages found with the given subject.")

result, message_content = M.fetch(message_id, '(RFC822)') #RFC822 is a protocol to fetch the Email data

raw_email = message_content[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == 'text/html':  #for pure text, we can use text/plain
        body = part.get_payload(decode=True)
        print(body)