import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import calendar
from datetime import datetime
#from picamera import PiCamera
mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'lkaae15@gmail.com'
sender_pass = 'Djh2020Miracs'
receiver_address = 'webmaster@pensionmira.dk'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

d = datetime.today()

date = str(d.month) + "_" + str(d.day) + "_" + str(d.year) + "_" + str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)

filename=date
f=open(filename, "w")
string=date+"\n"
f.write(string)
f.close()

attach_file_name = filename
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
