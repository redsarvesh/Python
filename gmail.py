#!/usr/bin/python
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com:587')
 
# start TLS for security
s.ehlo()
s.starttls()
sender_email_id='xxx@gmail.com'
sender_email_id_password='xxxxxxxxxxx'
# Authentication
s.login(sender_email_id, sender_email_id_password)
 
# message to be sent
message = "Messages"
receiver_email_id='xyz@gmail.com'
 
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
 
# terminating the session
s.quit()          
