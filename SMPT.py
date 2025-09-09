# smtp_client.py
import smtplib
import logging
from email.message import EmailMessage

# Configure logging
logging.basicConfig(filename="smtp_client.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def send_email():
    smtp_server = "localhost"
    smtp_port = 1025  # Debug SMTP server port

    sender = "sender@example.com"
    recipient = "recipient@example.com"

    # Create email message
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = "Test Email via Python SMTP"
    msg.set_content("Hello! This is a test email sent from Python.")

    try:
        logging.info("Connecting to SMTP server %s:%s", smtp_server, smtp_port)
        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            logging.info("Connected: %s", server.noop())
            server.send_message(msg)
            logging.info("Email sent successfully from %s to %s", sender, recipient)
        print("Email sent! (Check debug server terminal output)")
    except Exception as e:
        logging.error("SMTP error: %s", e)
        print("Failed to send email. See smtp_client.log for details.")

if __name__ == "__main__":
    send_email()
