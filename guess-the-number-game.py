import random


def guess_the_number():
    secret_number = random.randint(1, 10)
    max_attempts = 5
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    player_name = input("Enter your name: ")
    print(f"Hi {player_name}! I have I have selected a number between 1 and 10.")
    print("You have", max_attempts, "attempts to guess the correct number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print("Congratulations! You guessed the correct number in", attempts, "attempts.")
                break
            elif guess < secret_number:
                print("Incorrect, try again. The secret number is higher than your guess.")
            else:
                print("Incorrect, try again. The secret number is lower than your guess.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempts == max_attempts:
        print(f"Sorry, {player_name}, Game Over. No more attempts available. The secret number was", secret_number)
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print(f"Thank you for playing, {player_name}! :) Goodbye!")


if __name__ == "__main__":
    guess_the_number()
