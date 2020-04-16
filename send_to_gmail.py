'''
Send email to gmail account
'''
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

def send_to_gmail(subject, text):
    ''' Send email from test account '''
    port = 465  # For SSL
    load_dotenv()
    password = os.environ['TEST_GM_PW']
    sender_email = os.environ['SENDER_EMAIL']
    receiver_email = os.environ['RECEIVER_EMAIL']

    context = ssl.create_default_context()


    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText(text, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
