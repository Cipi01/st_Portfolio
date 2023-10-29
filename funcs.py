import smtplib
import ssl
from email.message import EmailMessage


def send_email(user_email, message_raw, gmail_pass):

    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg.set_content(message_raw + '\n' + user_email)

    msg['Subject'] = f'New email from {user_email}'
    msg['From'] = user_email
    msg['To'] = "cipi01work@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login("cipi01work@gmail.com", gmail_pass)
        server.send_message(msg)