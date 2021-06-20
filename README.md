# emailvalidation
Command line utility to validate email addresses.

If you don't want to install any packages, run without any flags. For more robust validation, install with
`pip install -r reqirements`
and run with the `-d` flag.

For extreme confirmation, run with the `-g` flag and specify a gmail account to use to send a confirmation email. This is the weirdest method of doing this via command line, but it is the most accurate one. I do not recommend it.

usage: emailvalidation.py [-h] [-g] [-es] [-esp] [-d] email

positional arguments:
  email                 email adress to validate

optional arguments:
  -h, --help            show this help message and exit
  -g, --guaranteed      Guarantee validation by sending a confirmation email and waiting for response. Requires a gmail account for sending mail.
  -es , --email_server_account
                        Gmail server account to use for email confirmation sendout
  -esp , --email_server_password
                        Gmail Server account password
  -d, --use_dependency  use the email-validator package to validate the email