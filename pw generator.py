import random
import string

def generate_password(length):
    # Choose on the password's character set.
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine every character set.
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Apply random.sample to produce a password with the length.
    password = ''.join(random.sample(all_characters, length))

    return password

def main():
    # Ask the user how long should be a password.
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Enter a valid number.")
        return

    # Check if the length is greater than 0
    if length <= 0:
        print("Enter a positive number for the password length.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
