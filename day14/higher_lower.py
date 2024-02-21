from higher_lower_art import logo, vs
from higher_lower_data import data
import random
import os


os.system("cls")
print(logo)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"Compare A: {name}, {description}, from {country}."


def play():
    game_over = False
    compare_data = random.choice(data)
    result_message = ""
    result_score = 0
    while not game_over:
        against_data = random.choice(data)
        while compare_data == against_data:
            against_data = random.choice(data)

        print(f"Compare A: {format_data(compare_data)}")
        print(vs)
        print(f"Against B: {format_data(against_data)}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        while answer not in ["a", "b"]:
            answer = input("Invalid input. Type 'A' or 'B': ").lower()

        os.system("cls")
        print(logo)
        if (
            answer == "a"
            and compare_data["follower_count"] < against_data["follower_count"]
        ) or (
            answer == "b"
            and against_data["follower_count"] < compare_data["follower_count"]
        ):
            result_message = "Sorry, that's wrong. "
            game_over = True
        else:
            result_score += 1
            print(f"You're right! Current score: {result_score}.")
            compare_data = against_data

    os.system("cls")
    print(logo)
    print(f"{result_message} Final score: {result_score}")


play()
