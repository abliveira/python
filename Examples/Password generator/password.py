# Programmable Password Generator
# by abliveira

import argparse
import random
import string

parser = argparse.ArgumentParser(description="less script")
# In the mode below, if the argument is not given, it is assumed to be false.
# parser.add_argument('-s', action='store_true', help="input file containing text to be formatted")
parser.add_argument('-s', '--special', help="input file containing text to be formatted")
parser.add_argument('-d', '--digits', help="input file containing text to be formatted")
parser.add_argument('-c','--case', help="input file containing text to be formatted")
parser.add_argument('-l', '--length', type=int, help="input length for the base character quantity per line")
args = parser.parse_args()
print (args)

# By default, it will generate a password between 6 and 16 characters
if args.length == None:
    pass_length = random.randint(6, 16)
else:
    pass_length = args.length

components = []   

#  "By default, it will generate a password with digits
if args.digits == 'nodigits':
  components.append()
elif args.digits == 'digits':
  components.append(string.digits)
else: # == None
  components.append(string.digits)

# By default, it will generate a password with lowercase and uppercase letters
if args.case == 'lower':
  components.append(string.ascii_lowercase)
elif args.case == 'upper':
  components.append(string.ascii_uppercase)
else: # == None
  components.append(string.ascii_letters)

# "By default, it will generate a password with special characters
if args.special == 'letters' or args.special == 'simple':
  components.append()
elif args.special == 'special' or args.special == 'complex':
  components.append("!@#$%&")
else:
  components.append("!@#$%&")

print(components)
# flatten the components into a list of characters
chars = []
for clist in components:
  for item in clist:
    chars.append(item)
def generate_password():
  # Store the generated password
  password = []
  # Choose a random item from 'chars' and add it to 'password'
  for i in range(pass_length):
    rchar = random.choice(chars)
    password.append(rchar)
  # Return the composed password as a string
  return "".join(password)

# Output generated password
print(generate_password())