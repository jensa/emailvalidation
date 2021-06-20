from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-g", "--guaranteed", action="store_true", help="Guarantee validation by sending a confirmation email and waiting for response")
parser.add_argument("email", help='email adress to validate')

args = parser.parse_args()
print(args.guaranteed)
print(args.email)

