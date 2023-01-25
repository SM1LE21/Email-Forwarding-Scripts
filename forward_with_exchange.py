#!/usr/bin/env python3
from datetime import datetime
from exchangelib import DELEGATE, Account, Credentials, Configuration, Message
import time

def forward_emails(username, password, forward_to_address, email):

    print("\nForwarding Script started\n")
    print("from: ", email ,"\nto: ", forward_to_address, "\n")

    # Connect to account1's inbox
    # Use the mail server of your email adress in the config part
    credentials = Credentials(username=username, password=password)
    config = Configuration(server='mail.example.com', credentials=credentials)
    account = Account(primary_smtp_address=email, config=config, autodiscover=False, access_type=DELEGATE)

    print("Inbox connection success\n")

    while True:
        # Search for all unread emails
        unread_emails = account.inbox.filter(is_read=False)

        # Forward each unread email
        for email_message in unread_emails:
           
            # Check if there is a subject, if not give it a value so the script does not crash
            if email_message.subject is None:
                email_message.subject = "The original email had no subject."

            # Check if the email has a body, if not give it a value so the script does not crash
            if email_message.text_body is None:
                email_message.text_body = "The original email had no text_body."

            # Check if the email has attatchments
            if email_message.attachments:
                attachments_temp = email_message.attachments
            else:
                attachments_temp = []

            # Create the forward email
            msg = Message(
                account=account,
                subject=f'FW: {email_message.subject}',
                body=email_message.text_body,
                to_recipients=[forward_to_address],
                #cc_recipients=email_message.cc,
                #bcc_recipients=email_message.bcc,
                attachments=attachments_temp,
            )

            msg.send()
            email_message.is_read = True
            email_message.save()

            print("________________\nemail forwarded\n_______________")

        print("Last refresh: ", datetime.now().strftime("%H:%M:%S"))

        # Sleep for 60 seconds before checking for new emails again
        time.sleep(60)

forward_emails("account_username@gmail.com", "account_password", "example@example.com", "email")


