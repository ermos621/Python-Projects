from email import message
from http import server
from re import sub
import smtplib
import ssl
from email.message import EmailMessage

'''
The program have written to send email via python . The code is self
explanatory.To achieve that a change from the setting of Gmail account
must change.

-> Manager account -> Security -> Enable "Less Secure app access"
'''

subject = " Enter your subject "
body = " Please enter your message"
sender_email = "enter the sender's email "
receiver_email = "enter receiver's email "
password = input("Enter a password : ")
'''
Please enter the password of the email account of the sender.
'''
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("sending email")

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())

print("Success")
