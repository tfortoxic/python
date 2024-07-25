import random
import string

# Function to generate random 3-letter strings
def generate_random_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(3))

# Function to encode the message
def encode_message(original_msg):
    random_prefix = generate_random_string()
    random_suffix = generate_random_string()
    coded_msg = random_prefix + original_msg + random_suffix
    print("Your coded message is:", coded_msg)

# Function to reverse the message and display the encoded message
def reverse_and_encode(original_msg):
    reversed_msg = original_msg[::-1]
    encode_message(reversed_msg)

# Function to decode the message and display the original message
def decode_message(encoded_msg):
    original_msg = encoded_msg[3:-3]  # Removing random prefixes and suffixes
    first_letter = original_msg[0]  # Extracting the first letter of the original message
    rest_of_msg = original_msg[1:]  # Extracting the rest of the original message
    decoded_msg = first_letter + rest_of_msg
    print("Your decoded message is:", decoded_msg)

# Main function for user input and program flow
def user_input():
    print("WELCOME TO SECRET MESSAGE ENCODER/DECODER")
    user_choice = input("For encoding, press 'E'. For decoding, press 'D': ").replace(" ", "").upper()  # Removing spaces from user input
    
    if user_choice == 'E':
        original_msg = input("Enter the message you want to encode: ").replace(" ", "")  # Removing spaces from user input
        if len(original_msg) <= 3:
            reverse_and_encode(original_msg)
        else:
            encode_message(original_msg)
    elif user_choice == 'D':
        encoded_msg = input("Enter the encoded message to decode: ").replace(" ", "")  # Removing spaces from user input
        decode_message(encoded_msg)
    else:
        print("Invalid choice. Please enter 'E' for encoding or 'D' for decoding.")

# Calling the main function to start the program
user_input()