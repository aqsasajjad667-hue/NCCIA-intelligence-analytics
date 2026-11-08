import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Agar aap ke paas gemini ya koi aur library use ho rahi hai, wohi rehne dein

def send_email_report(report_content):
    # GitHub Secrets se email credentials uthaye ga
    sender_email = os.environ.get("EMAIL_USER")
    sender_password = os.environ.get("EMAIL_PASSWORD")
    receiver_email = sender_email  # Aap apni hi email par receive kar sakti hain
    
    if not sender_email or not sender_password:
        print("Email credentials not found in environment variables!")
        return

    # Email message setup
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "NCCIA Daily Intelligence Report"

    msg.attach(MIMEText(report_content, 'plain'))

    try:
        # Gmail SMTP server connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email report sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Aap ka main logic yahan chalega
if _name_ == "_main_":
    print("--- Running NCCIA Intelligence Agent ---")
    
    # Farz karein yeh aap ka extracted data ya report hai
    extracted_data = """
    NCCIA Intelligence Summary:
    - Raids: Not Reported
    - Arrests: Not Reported
    - FIRs: Not Reported
    """
    
    # Data extract hone ke baad email send karne wala function call kar dein
    send_email_report(extracted_data)
  
