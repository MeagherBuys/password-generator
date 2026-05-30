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

    elif mode == 3:
        pool = letters + numbers + symbols
        guaranteed.append(random.choice(string.ascii_uppercase))
        guaranteed.append(random.choice(numbers))
        guaranteed.append(random.choice(symbols))

    password = guaranteed.copy()

    for _ in range(length - len(guaranteed)):
        password.append(random.choice(pool))

    random.shuffle(password)
    return "".join(password)


while True:
    print("\nPassword Generator Menu")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        print("\nPassword Strength Options")
        print("1. Letters only")
        print("2. Letters + Numbers")
        print("3. Letters + Numbers + Symbols")

        mode = input("Choose mode (1-3): ")

        if mode not in ["1", "2", "3"]:
            print("Invalid mode selected.")
            continue

     
        while True:
            try:
                length = int(input("Password length: "))

                if length < 3:
                    print("Length too short. Must be at least 3.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        password = generate_password(length, int(mode))
        print("Generated Password:", password)

    elif choice == "2":
        print("Goodbye! Exiting Password Generator...")
        break

    else:
        print("Invalid menu option. Try again.")