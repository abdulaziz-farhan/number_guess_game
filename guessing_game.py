import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Maximum number of attempts
max_attempts = 7

print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.")

won = False

# Give the user multiple attempts
for attempt in range(1, max_attempts + 1):

    guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly!")
        won = True
        break

    # Check if the guess is too high
    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    # Otherwise, the guess is too low
    else:
        print("Too low! Try a larger number.")

# If the user did not guess correctly
if not won:
    print(f"Game over! The number was {secret_number}.")