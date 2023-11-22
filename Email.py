# Email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_addr):
    from_addr = "YOUR@EMAIL.ID"

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the email account
        server.login(from_addr, "EMAIL_PASSWORD")  # Replace "PASSWORD" with the actual password

        # Convert the message to a string and send the email
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)

#        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    finally:
        # Quit the server regardless of success or failure
        server.quit()