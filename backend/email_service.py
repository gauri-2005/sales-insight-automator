import smtplib
from email.mime.text import MIMEText

def send_email(receiver, summary):

    sender = "gauri.saini.125@gmail.com"
    password = "uczi msps fkqw ptbk"

    msg = MIMEText(summary)

    msg["Subject"] = "Sales Summary"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, receiver, msg.as_string())

    server.quit()