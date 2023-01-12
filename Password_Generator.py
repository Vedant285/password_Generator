import random
import string

def generate_password(length):
    # Get a random selection of letters, digits, and special characters
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Example usage
print(generate_password(16))
