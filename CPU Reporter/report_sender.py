import smtplib
import ssl
import os

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


email = "test@gmail.com"  # your email
password = "password"  # your password

message = MIMEMultipart("alternative")
message["From"] = 'един приятел'
message["To"] = 'теб'


def send_text_email(report, generation_seconds: int):
    
    message["Subject"] = f"{generation_seconds} Seconds CPU Report"

    to_send = MIMEText(report, "plain")
    message.attach(to_send)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:

        server.login(email, password)
        server.sendmail(email, email, message.as_string())


def send_pdf_email(report: None, generation_seconds: int):
    message["Subject"] = f"{generation_seconds} Seconds CPU Report"
    
    with open('image_to_send.png', "rb") as attachment:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= image_to_send.png",
    )

    message.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:

        server.login(email, password)
        server.sendmail(email, email, message.as_string())

    os.remove('image_to_send.png')
