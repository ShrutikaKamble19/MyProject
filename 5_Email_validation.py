import re

def validate_email(email):
    """
    Validates an email address using a regular expression.
    
    Parameters:
        email (str): The email address to validate.
        
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression pattern for validating an email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    return bool(re.match(email_pattern, email))

def main():
    print("Welcome to the Email Validator!")
    
    while True:
        # Get user input
        email = input("Enter an email address to validate (or type 'exit' to quit): ").strip()
        
        # Check if the user wants to exit
        if email.lower() == 'exit':
            print("Exiting the Email Validator. Goodbye!")
            break
        
        # Validate the email and display the result
        if validate_email(email):
            print(f"'{email}' is a valid email address.\n")
        else:
            print(f"'{email}' is not a valid email address. Please try again.\n")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
