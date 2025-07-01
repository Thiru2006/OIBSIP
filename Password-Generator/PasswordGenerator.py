import random
import string
try:
    length = int(input("Enter desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("No character types selected. Cannot generate password.")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}")

except ValueError:
    print("Please enter a valid number for the password length.")
