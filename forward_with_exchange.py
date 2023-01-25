#!/usr/bin/env python3
from datetime import datetime
from exchangelib import DELEGATE, Account, Credentials, Configuration, Message, FileAttachment, ItemAttachment
import time
import os.path

def forward_emails(username, password, forward_to_address, email, mail_server):

    print("\nForwarding Script started\n")
    print("from: ", email ,"\nto: ", forward_to_address, "\n")

    # Connect to account1's inbox
    credentials = Credentials(username=username, password=password)
    config = Configuration(server=mail_server, credentials=credentials)
    account = Account(primary_smtp_address=email, config=config, autodiscover=False, access_type=DELEGATE)

    print("\nInbox connection success\n")

    while True:

        # Search for all unread emails
        unread_emails = account.inbox.filter(is_read=False)

        # Forward each unread email
        for email_message in unread_emails:

            # Check if there is a subject, if not give it a value so the script does not crash
            if email_message.subject is None:
                email_message.subject = "(no subject)"

            # Check if the email has a body, if not give it a value so the script does not crash
            if email_message.text_body is None:
                email_message.text_body = "(no textBody)"

            # Create the forward email
            msg = Message(
                account=account,
                subject=f'FW: {email_message.subject}',
                body=email_message.text_body,
                to_recipients=[forward_to_address],
                #cc_recipients=email_message.cc,
                #bcc_recipients=email_message.bcc,
            )

            
            # Here we attach any attachments if there are attachments
            # Attention! Attachments are saved locally and will then be forwarded
            for attachment in email_message.attachments:
                if isinstance(attachment, FileAttachment):
                    local_path = os.path.join('/tmp', attachment.name)
                    with open(local_path, 'wb') as f:
                        f.write(attachment.content)
                    with open(local_path, 'rb') as f:
                        my_attachment = FileAttachment(
                            name=local_path,
                            content=f.read(),
                            is_inline=True,
                            content_id=local_path
                        )
                    msg.attach(my_attachment)
                    print('Saved attachment to', local_path)
                elif isinstance(attachment, ItemAttachment):
                    if isinstance(attachment.item, Message):
                        print(attachment.item.subject, attachment.item.body)
                
            
            msg.send()
            email_message.is_read = True
            email_message.save()

            print("--------------------\nemail forwarded\n--------------------")

        print("Last refresh: ", datetime.now().strftime("%H:%M:%S"))

        # Sleep for 60 seconds before checking for new emails again
        time.sleep(60)


forward_emails("account_username", "account_password", "example@example.com", "email", "mail.example.com")

