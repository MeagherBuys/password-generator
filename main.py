import random
import string

def generate_password(length, mode):
    if mode == 1:
        characters = string.ascii_letters
    elif mode == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("Password Generator")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

mode = int(input("Choose option (1-3): "))
length = int(input("How long should your password be? "))

password = generate_password(length, mode)

print("Generated Password:", password)