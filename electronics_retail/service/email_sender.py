import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

from electronics_retail.service import generate_qr_code
from retail_app.celery import app

load_dotenv()

smtp_port = int(os.environ.get('SMTP_PORT'))
smtp_server = os.environ.get('SMTP_SERVER')
email_from = os.environ.get('EMAIL_FROM')
PSWD = os.environ.get('PSWD')


@app.task
def send_email(email_to, qr_data):
    print(email_to)
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = ', '.join(email_to)
    msg['Subject'] = 'QR Code(Retail application)'

    qr_code_data = generate_qr_code(qr_data)
    if qr_code_data:
        image = MIMEImage(qr_code_data)
        msg.attach(image)

    mail_server = smtplib.SMTP(smtp_server, smtp_port)
    try:
        mail_server.starttls()
        mail_server.login(email_from, PSWD)
        mail_server.sendmail(email_from, email_to, msg.as_string())
    except smtplib.SMTPRecipientsRefused as e:
        problematic_emails = [addr for addr, error in e.recipients.items()]
        print(f"Email sending failed for: {problematic_emails}")
        print(f"SMTPRecipientsRefused error: {e}")
    finally:
        mail_server.quit()

