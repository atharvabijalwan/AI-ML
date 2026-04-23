import random

def start_game():
    print("--- Welcome to the Number Guessing Game! ---")
    # Generate a random number between 1 and 1000
    secret_number = random.randint(1, 1000)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 1000.")

    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    start_game()