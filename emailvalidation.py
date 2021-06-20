from argparse import ArgumentParser
import re
parser = ArgumentParser()
parser.add_argument("-g", "--guaranteed", action="store_true", help="Guarantee validation by sending a confirmation email and waiting for response. Requires a gmail account for sending mail.")
parser.add_argument("-es", "--email_server_account", metavar="", help="Gmail server account to use for email confirmation sendout")
parser.add_argument("-esp", "--email_server_password", metavar="", help="Gmail Server account password")
parser.add_argument("-d", "--use_dependency", action="store_true", help="use the email-validator package to validate the email")
parser.add_argument("email", help='email adress to validate')

args = parser.parse_args()

if args.use_dependency:
    from email_validator import validate_email, EmailNotValidError
    try:
      validate_email(args.email)
      print("valid")
    except EmailNotValidError as e:
      print("invalid")
    finally:
        exit()      
if args.guaranteed:
    import smtplib, ssl
    port = 465  # For SSL
    email_server_acc = args.email_server_account if args.email_server_account else input("Gmail address (for sending confirmation email):")
    password = args.email_server_password if args.email_server_password else input("Password:")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=ssl.create_default_context()) as server:
        server.login(email_server_acc, password)
        message = f"""\
        Confirm email

        Hello!
        
        I'm going to need you to confirm your email. 
        Since I wouldnt want to set up a http server here just to wait for your response, 
        you can simply email me at {email_server_acc} with the string "valid". 
        I will interpret a non-response within 24 hours as an invalid email. Thanks!
        """
        server.sendmail(email_server_acc, args.email, message)
        exit()    
    
#https://en.wikipedia.org/wiki/Email_address#Valid_email_addresses
# this regex is _not_ complete (exludes explicit ip adresses in domain part, fails quoted strings for local part, fails comments)
local_part = "(^[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~][a-zA-Z0-9!#$%&'*+-/=?^_`{|}~.]*"
dns_list = "@([a-zA-Z0-9]+[a-zA-Z0-9-]*.)*([a-zA-Z0-9]+[a-zA-Z0-9-]*)+$)"
very_simple_regex = local_part + dns_list
match = re.search(very_simple_regex, args.email)
no_double_dots = not re.search("\.\.", args.email)
print("valid" if match and no_double_dots else "invalid")

