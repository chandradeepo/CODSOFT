import random
import string

while True:

    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("Length must be greater than 0")
            continue

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ""

        for _ in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break

    except ValueError:
        print("Please enter a valid number.")