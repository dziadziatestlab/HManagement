import smtplib
import os.path
from email.mime.text import MIMEText
msg=MIMEText("Message")
msg['Subject']="Subject"
msg['From']='From'
s=smtplib.SMTP_SSL('server:port')
s.login('login','pass')
s.sendmail('From','To',msg.as_string())
s.quit()
