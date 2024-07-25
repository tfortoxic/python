import random
import string

# Function to encode the message
def coding(changed_str):
    # Generating random 3-letter strings for encryption
    str1 = "".join(random.choice(string.ascii_lowercase) for i in range(3))
    str2 = "".join(random.choice(string.ascii_lowercase) for i in range(3))
    
    # Creating the coded message by concatenating random strings and the input message
    coded_msg = str1 + changed_str + str2
    print("Your coded message is:", coded_msg)

# Function for encoding a message
def forcoading_msg():
    msg = input("Enter a message you want to encrypt: ").replace(" ", "")  # Removing spaces from user input
    
    # If the message is 3 characters or less, reverse the message for encryption
    if len(msg) <= 3:
        rev = msg[::-1]
        forstring(rev)
    else:
        msg1 = msg[0]
        msg = msg.replace(msg[0], "")
        changed_str = msg + msg1
        coding(changed_str)

# Function to decode the message
def fordcoading_msg():
    dmsg = input("Enter the encrypted message to decrypt: ").replace(" ", "")  # Removing spaces from user input
    new_msg = dmsg[3:-3]  # Removing the random strings from the encrypted message
    a = new_msg[-1]  # Extracting the first character of the original message
    new_msg = new_msg.replace(new_msg[-1], "")  # Removing the first character from the rest of the message
    print("your decrypted message is: ",a + new_msg)

# Function for displaying the encoded message
def forstring(rev):
    print("Your coded message is:", rev)

# Main function for user input and program flow
def user_input():
    print("THIS IS A PROGRAM TO ENCRYPT AND DECRYPT THE MESSAGE")
    user_preference = input("For coding, press C. For decoding, press D: ").replace(" ", "")  # Removing spaces from user input
    inp = user_preference.upper()
    if inp == "C":
        forcoading_msg()
    elif inp == "D":
        fordcoading_msg()
    else:
        print("Invalid input! Please enter C for coding or D for decoding.")
        user_input()

# Calling the main function to start the program
user_input()