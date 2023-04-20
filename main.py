# Password Generator

# Import modules
import time
import random
import string as str

# Create string with all acceptable characters
letters = str.ascii_letters
digits = str.digits
punctuation = str.punctuation
acceptable_characters = letters + digits + punctuation

# Returns random password
def generatepassword(length):
    password_new = ""
    # Loop through to create password
    for x in range(0,int(length)):
        new_letter = random.choice(acceptable_characters)
        password_new += new_letter

    return password_new

    print(new_letter)
# Main
if __name__ == '__main__':
    # Get parameters
    print("This is a password generator.")
    time.sleep(1)
    length = input("What length password do you want? ")
    print(generatepassword(length))