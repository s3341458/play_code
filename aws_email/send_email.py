import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("./smtp.cfg") as config_file:
    config = json.loads(config_file.read())

# AWS Config
EMAIL_HOST = config["smtp_host"]
EMAIL_PORT = config["smtp_host_port"]
EMAIL_HOST_USER = config["smtp_host_username"]
EMAIL_HOST_PASSWORD = config["smtp_host_password"]

msg = MIMEMultipart('alternative')
msg['Subject'] = "lele test mail"
msg['From'] = "chengyu0316@gmail.com"
msg['To'] = "chengyu0316@gmail.com"

html = open(__file__).read()

mime_text = MIMEText(html, 'html')
print("debug here mime text", mime_text)
msg.attach(mime_text)

s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
s.starttls()
s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
s.sendmail("chengyu0316@gmail.com", "chengyu0316@gmail.com", msg.as_string())
s.quit()
