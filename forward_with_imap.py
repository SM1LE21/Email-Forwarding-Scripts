#!/usr/bin/env python3
import imaplib
import email
import smtplib
import time
from datetime import datetime

def forward_emails(account_username, account_password, forward_to_address):

    print("\nForwarding Script started\n")
    print("from: ", account_username ,"\nto: ", forward_to_address, "\n")

    # 
    # Connect to account's inbox 
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(account_username, account_password)
    mail.select("inbox")

    print("Imap success\n")

    # Connect to smtp server
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(account_username, account_password)

    print("Smtp success \n")

    while True:
        # Search for all unread emails
        result, data = mail.search(None, "UNSEEN")
        unread_emails = data[0].split()

        # Forward each unread email
        for email_id in unread_emails:
            result, data = mail.fetch(email_id, "(RFC822)")
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)

            # Send the email
            smtp.sendmail(account_username, forward_to_address, email_message.as_string())

        # Sleep for 60 seconds before checking for new emails again

        print("Last refresh: ", datetime.now().strftime("%H:%M:%S"))
        
        time.sleep(60)

forward_emails("account_username@gmail.com", "account_password", "example@example.com")
