import poplib
import email
import smtplib
import time
from datetime import datetime

def forward_emails(account_username, account_password, forward_to_address):

    print("\nForwarding Script started\n")
    print("from: ", account_username ,"\nto: ", forward_to_address, "\n")

    # Here we use gmail a gmail acount, change the pop/smtp server if needed
    # Connect to account1's inbox
    mail = poplib.POP3_SSL("pop.gmail.com")
    mail.user(account_username)
    mail.pass_(account_password)

    print("Pop success\n")

    # Connect to smtp server
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(account_username, account_password)

    print("Smtp success \n")

    while True:
        # Get the number of new emails
        new_emails = len(mail.list()[1])

        for i in range(new_emails):
            # Get the raw email data
            msg = mail.retr(i+1)[1]

            # Concatenate the message parts
            msg_str = "".join(map(str, msg))

            # Create the email message
            msg = email.message_from_string(msg_str)

            # Send the email
            smtp.sendmail(account_username, forward_to_address, msg.as_string())

            # Delete the email from the server
            # This part is necessary in this example otherwise the script
            # will keep sending the same mails. There are of course other options
            # an example is shown in the forward_with_imap.py file.
            mail.dele(i+1)

        # Sleep for 60 seconds before checking for new emails again

        print("Last refresh: ", datetime.now().strftime("%H:%M:%S"))
        
        time.sleep(60)

forward_emails("account_username@gmail.com", "account_password", "example@example.com")
