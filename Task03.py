import random
import string

def generate_password(length=int(input("enter length of password"))):
    if length < 8:
        return "Password length must be at least 8 characters"
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    password = []
    password.extend(random.choice(uppercase_letters) for _ in range(2))
    password.extend(random.choice(lowercase_letters) for _ in range(2))
    password.extend(random.choice(digits) for _ in range(2))
    password.extend(random.choice(special_characters) for _ in range(2))
    
    while len(password) < length:
        random_character = random.choice(uppercase_letters + lowercase_letters + digits + special_characters)
        password.append(random_character)
    
    random.shuffle(password)
    return ''.join(password)

password = generate_password()

print("Generated Password:", password)
                      