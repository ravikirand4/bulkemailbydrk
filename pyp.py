import smtplib
from email.mime.text import MIMEText
import csv

# Function to send email
def send_email(sender_email, sender_password, recipient_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    server = smtplib.SMTP_SSL('smtp.zoho.in', 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Function to read CSV file and send emails
def send_bulk_emails(sender_email, sender_password, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipient_email = row['Email']
            subject = row['Subject']
            message = row['Message']
            # You can customize the message here to include the recipient's name if needed
            send_email(sender_email, sender_password, recipient_email, subject, message)

# Sender E-mail Id and password
sender_email = 'dikondaravikiran@zohomail.in'
sender_password = 'We66NpT7X3Gs'

# Path to CSV file
csv_file = r'c:\Users\Arun\Downloads\Sample Bulk Email - Sheet1.csv'

# Sending bulk emails
send_bulk_emails(sender_email, sender_password, csv_file)
