# Email-Forwarding-Scripts
this repository contains three scripts that can be used to automatically forward emails from different email protocols (IMAP, POP, and Exchange) to a specified email address.

## forward_with_exchange.py
This script uses the `exchangelib` library to log in to an Exchange email account and continuously monitor for new emails. Each new email is forwarded as soon as it arrives to the specified email address.

## forward_with_imap.py
This script uses the `imaplib` library to log in to an email account that supports the IMAP protocol and continuously monitor for new emails. Each new email is forwarded as soon as it arrives to the specified email address.

## forward_with_pop.py
This script uses the `poplib` library to log in to an email account that supports the POP3 protocol and continuously monitor for new emails. Each new email is forwarded as soon as it arrives to the specified email address.

# Usage 
To use these scripts, you will need to replace the placeholders for `username`, `password`, and `forward_to_address` with the actual login credentials for your email account and the address you want to forward the emails to.

You will also need to install the necessary libraries for each script, please refer to the `requirements.txt` file for more details on the dependencies.

Please be aware that these scripts will be running indefinitely, you can use a tool like `screen` or `nohup` to keep the script running in the background.

Also, please note that these scripts will be checking the email inbox every minute, but the delay of receiving the email on the other account may be different based on many factors such as the email server, internet connection etc.

If you're using gmail, you might need to enable less secure apps and create an application specific password as explained in the script comments.

Also, please check the server address, port number, and the type of encryption in use with your server administrator.

Please refer to the script comments for more details on usage and configuration.

Enjoy!
