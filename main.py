# Password Generator

# Import modules
import time
import random
import string as str

# Create string with all acceptable characters
acceptable_characters = str.ascii_letters + str.digits + str.punctuation

def generatepassword(length):

    new_letter = random.choice(acceptable_characters)
    print(f'Here is your password of length {length}')
    print(new_letter)
# Main
if __name__ == '__main__':
    # Get parameters
    print("This is a password generator.")
    time.sleep(1)
    length = input("What length password do you want? ")
    generatepassword(length)