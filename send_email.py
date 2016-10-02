# Adapted from http://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp

import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()

message_file = 'example.txt'
fp = open(message_file, 'rb')
msg = MIMEText(fp.read())
fp.close()

msg['From'] = 'harini.automated@gmail.com'
msg['To'] = 'hariniharini@gmail.com'

now = datetime.datetime.now()
date = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
msg['Subject'] = 'What you did today (' + date + ') :)' 

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()

credentials_file = 'email.txt'
credentials = open(credentials_file).readlines()
email_address = credentials[0].strip()
password = credentials[1].strip()

mailserver.login(email_address, password)

mailserver.sendmail('hariniharini@gmail.com','hariniharini@gmail.com', msg.as_string())

mailserver.quit()
