import random
import string

def generate_password(length, mode):
    
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    pool = ""
    guaranteed = []

    
    if mode == 1:
        pool = letters
        guaranteed.append(random.choice(string.ascii_uppercase))

    elif mode == 2:
        pool = letters + numbers
        guaranteed.append(random.choice(string.ascii_uppercase))
        guaranteed.append(random.choice(numbers))

    else:
        pool = letters + numbers + symbols
        guaranteed.append(random.choice(string.ascii_uppercase))
        guaranteed.append(random.choice(numbers))
        guaranteed.append(random.choice(symbols))

    
    password = guaranteed.copy()

    for _ in range(length - len(guaranteed)):
        password.append(random.choice(pool))

    
    random.shuffle(password)

    return "".join(password)


print("Password Generator (Strong Mode)")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

mode = int(input("Choose option (1-3): "))
length = int(input("Password length: "))

if length < 3:
    print("Length too short for strong password rules.")
else:
    password = generate_password(length, mode)
    print("Generated Password:", password)