import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

        try:
            # Log in to the server
            print("logging in")
            server.login(sender_email, sender_password)
            print("sending")
            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            # Disconnect from the server
            server.quit()

# Example usage
sender_email = 'biobrief7@gmail.com'
sender_password = 'uath yvmk lxvj tjhn'
recipient_email = 'zesun@ucsd.edu'
subject = 'Hello world'
body = 'qwqwqwqwqwq\n pwpwpwpwpwp\n owowowowowo\n'

send_email(sender_email, sender_password, recipient_email, subject, body)