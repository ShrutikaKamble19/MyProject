import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Define character sets for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password has at least one character from each category
    all_chars = lowercase + uppercase + digits + special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the rest of the password length with random choices from all character sets
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

# Example usage
password = generate_password(12)
print("Generated Password:", password)
