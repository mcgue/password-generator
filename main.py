# Password Generator

# Import modules
import time
import random
import string as str

acceptable_characters = str.ascii_letters + str.digits + str.punctuation

def generatepassword(max, min):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Here is your password with a maximum length of {max}')
    print(f'Here is your password with a minimum length of {min}')

# Main
if __name__ == '__main__':
    # Get parameters
    print("This is a password generator. Answer the following questions...")
    time.sleep(1)
    max_length = input("What is the maximum length? ")
    min_length = input("What is the minimum length? ")
    generatepassword(max_length, min_length)
    print(acceptable_characters)