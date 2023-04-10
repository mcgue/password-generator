# Password Generator

# Import modules
import time

def generatepassword(length):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Here is your password with a maximum length of {length}')

# Main
if __name__ == '__main__':
    print("This is a password generator. Answer the following questions:")
    time.sleep(1)
    max_length = input("What is the maximum length? ")
    min_length = input("What is the minimum length? ")
    generatepassword(max_length)

