import random

def play_guessing_game():
    target_number = random.randint(1, 9)
    max_attempts = 5

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 9.")

    for attempt in range(max_attempts):
        guess = int(input(f"\nAttempt {attempt + 1}/{max_attempts}. Enter your guess (between 1 and 9): "))

        if guess == target_number:
            print("Congratulations! You guessed the correct number!")
            return
        elif abs(guess - target_number) <= 2:
            print("You're very close to the correct number.")
        else:
            print("You're far from the correct number.")

    print(f"\nSorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")

if __name__ == "__main__":
    play_guessing_game()
