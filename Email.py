#  libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Email():
    
    fromaddr = "XYZ" #EMAIL address of the sender
    toaddr = "ZYZ" #EMAIL address of the receiver

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "SI-Alert: Automated Network Devices Backup Script Executed Successfully!!" # Subject of the Mail

    # string to store the body of the mail
    body = "Hello Team, \n \nAutomated script executed successfully to take the configuration backup of network devices listed below:- \n \n 2. Switch1 \n 3. Switch2 \n \nThank you! \n_ _ \nRegards, \nKishor Khande.\n--------------------------------------------------------------------------------------------------------\nThis is a system generated alert. Do not reply to this email. \n--------------------------------------------------------------------------------------------------------" # Body_of_the_mail

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # # open the file to be sent
    # filename = "File_name_with_extension"
    # attachment = open("Path of the file", "rb")

    # # instance of MIMEBase and named as p
    # p = MIMEBase('application', 'octet-stream')

    # # To change the payload into encoded form
    # p.set_payload((attachment).read())

    # # encode into base64
    # encoders.encode_base64(p)

    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # # attach the instance 'p' to instance 'msg'
    # msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "ABC") #Password_of_the_sender

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()


