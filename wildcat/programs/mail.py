import os, ssl, smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

email_sender = os.getenv("EMAIL", None)
email_password = os.getenv("EMAIL_PASSWORD", None)

def send_email(email_receiver, subject, body):
    message = EmailMessage()
    message['From']=email_sender
    message['To']=email_receiver
    message['Subject']=subject
    message.set_content(body)
    
    contex = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contex) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, message.as_string())