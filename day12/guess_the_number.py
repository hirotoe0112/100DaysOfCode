from guess_the_number_art import logo, you_win, you_lose
import random
import os

os.system("cls")

DIFFICULTY = {"easy": 10, "hard": 5, "hell": 1}


def play():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' or 'hell': ").lower()
    while difficulty not in DIFFICULTY:
        difficulty = input(
            "Invalid input. Choose a difficulty. Type 'easy' or 'hard': "
        ).lower()
    remaining_attempts = DIFFICULTY[difficulty]
    while remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if answer == user_guess:
            os.system("cls")
            print(you_win)
            print(f"You got it! The answer was {answer}.")
            return
        elif answer < user_guess:
            print("Too high.")
            remaining_attempts -= 1
        else:
            print("Too low.")
            remaining_attempts -= 1

        if remaining_attempts == 0:
            os.system("cls")
            print(you_lose)
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")


while (
    input("Do you want to play a game of Number Guessing? Type 'y' or 'n': ").lower()
    == "y"
):
    play()

print("Goodbye.")
