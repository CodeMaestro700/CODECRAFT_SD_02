import random

secret_number = random.randint(1, 100)
guess = None
attempts = 0

print("🎲 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! 🔽")
        elif guess > secret_number:
            print("Too high! 🔼")
    except ValueError:
        print("❗ Please enter a valid number.")

print(f"✅ Correct! The number was {secret_number}.")
print(f"🏁 You guessed it in {attempts} attempts.")
