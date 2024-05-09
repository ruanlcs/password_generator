import random

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains uppercase letters
    if not any(char.isupper() for char in password):
        return False
    
    # Check if the password contains lowercase letters
    if not any(char.islower() for char in password):
        return False
    
    # Check if the password contains numbers
    if not any(char.isdigit() for char in password):
        return False
    
    # Check if the password contains symbols
    symbols = "()[]{}<>,=^`;:.-_/\\?+*!@#$%&*|~"
    if not any(char in symbols for char in password):
        return False
    
    return True

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{}<>,=^`;:.-_/\\?+*!@#$%&*|~"

all_characters = ""
all_characters += uppercase_letters
all_characters += lowercase_letters
all_characters += digits
all_characters += symbols

while True:
    print("Choose an option:")
    print("1 - Test a password")
    print("2 - Generate a random password")
    print("3 - Exit")
    
    option = input("Option: ")
    
    if option == "1":
        user_password = input("Enter the password to be tested: ")
        if is_strong_password(user_password):
            print("Strong password!")
        else:
            print("Weak password. Please make sure your password is at least 8 characters long and contains uppercase and lowercase letters, numbers, and symbols.")
    elif option == "2":
        while True:
            length = int(input("Enter the length of the password (minimum 8 characters): "))
            if length >= 8:
                break
            else:
                print("Password length must be at least 8 characters.")
        
        password = "".join(random.sample(all_characters, length))
        print("Randomly generated password:", password)
        
        save_option = input("Do you want to save this password to a text file? (y/n): ")
        if save_option.lower() == "y":
            file_name = input("Enter the text file name to save the password: ")
            with open(file_name, "w") as file:
                file.write(password)
                print(f"Password successfully saved to the file {file_name}")
    elif option == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose one of the provided options.")
