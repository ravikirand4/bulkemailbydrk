# Bulk Email Sender

This Python script allows you to send bulk emails using a CSV file containing email addresses, subjects, and messages.
## VIDEO EXPLANATION
[VIDEO LINK](https://drive.google.com/file/d/1lnppb5ZXJQlZGOE7OjSqwGwqJmKFmJtA/view?usp=sharing)
## SETUP YOUR PC:
- install python in your PC.
- Open the VS CODE, and RUN the file
- Change the sender details accordingly.

## Dependencies

- **smtplib**: This library is used for sending email messages from a Python script.
- **MIMEText**: From the `email.mime.text` module, `MIMEText` is used to create email message objects.
- **csv**: This library is used to read CSV files.

## Functions

### `send_email(sender_email, sender_password, recipient_email, subject, message)`

This function sends an email using SMTP (Simple Mail Transfer Protocol).

- **Parameters**:
  - `sender_email`: The email address of the sender.
  - `sender_password`: The password of the sender's email account.
  - `recipient_email`: The email address of the recipient.
  - `subject`: The subject of the email.
  - `message`: The body of the email.

### `send_bulk_emails(sender_email, sender_password, csv_file)`

This function reads a CSV file containing email addresses, subjects, and messages, and sends emails to each recipient.

- **Parameters**:
  - `sender_email`: The email address of the sender.
  - `sender_password`: The password of the sender's email account.
  - `csv_file`: The path to the CSV file containing recipient details.

## Usage

1. Set the `sender_email` and `sender_password` variables to your email address and password.
2. Set the `csv_file` variable to the path of your CSV file containing recipient details.
3. Run the script to send bulk emails to the recipients specified in the CSV file.

Feel free to customize the sender's email address, password, CSV file path, and message content according to your requirements before running the script. If you have any questions or need further assistance, please don't hesitate to ask!
