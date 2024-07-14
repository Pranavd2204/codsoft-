import random
import string

def generate_password(length=12):
    """Generate a random password of a given length."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lower + upper + digits + symbols
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password
password = generate_password(16)  
print("Generated password is:", password)