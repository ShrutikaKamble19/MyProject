import getpass

def check_password(input_password, correct_password):
    """
    Checks if the input password matches the correct password.
    
    Parameters:
        input_password (str): The password entered by the user.
        correct_password (str): The correct password to access the system.
        
    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return input_password == correct_password

def main():
    correct_password = "SecurePass123"  # Set the correct password here
    
    print("Welcome to the Password Protected System!")
    
    # Loop until the user provides the correct password
    while True:
        # Get password input securely using getpass
        input_password = getpass.getpass(prompt="Enter your password: ")
        
        if check_password(input_password, correct_password):
            print("Password correct! Access granted.")
            # Place additional code here to grant access to the system after successful login
            break  # Exit loop after successful login
        else:
            print("Incorrect password. Please try again.")
    
if __name__ == "__main__":
    main()
