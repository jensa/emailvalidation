from argparse import ArgumentParser
import re
parser = ArgumentParser()
parser.add_argument("-g", "--guaranteed", action="store_true", help="Guarantee validation by sending a confirmation email and waiting for response")
parser.add_argument("-d", "--use_dependency", action="store_true", help="Guarantee validation by sending a confirmation email and waiting for response")
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
if not args.guaranteed:
    #https://en.wikipedia.org/wiki/Email_address#Valid_email_addresses
    # this regex is _not_ complete (exludes explicit ip adresses in domain part, fails quoted strings for local part, fails comments)
    local_part = "(^[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~][a-zA-Z0-9!#$%&'*+-/=?^_`{|}~.]*"
    dns_list = "@([a-zA-Z0-9]+[a-zA-Z0-9-]*.)*([a-zA-Z0-9]+[a-zA-Z0-9-]*)+$)"
    very_simple_regex = local_part + dns_list
    match = re.search(very_simple_regex, args.email)
    no_double_dots = not re.search("\.\.", args.email)
    print("valid" if match and no_double_dots else "invalid")
    exit()


    
    
    


