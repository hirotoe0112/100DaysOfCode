import os
import random
from hangman_art import stages, logo
from hangman_words import word_list, genres

os.system("cls")

print(logo)

# select genre
genre = random.randint(0, len(genres) - 1)
print(f"The word is related to {genres[genre]}")

# select word
word = random.choice(word_list[genre])

display = []
for _ in word:
    display.append("_")

end_of_game = False
lives = 6
while not end_of_game:
    user_answer = input("Guess a letter: ").lower()

    os.system("cls")

    if user_answer in display:
        print(f"You've already guessed {user_answer}")
    else:
        for index in range(0, len(display)):
            if word[index] == user_answer:
                display[index] = user_answer
        if user_answer not in word:
            print(
                f"You guessed {user_answer}, that's not in the word. You lose a life."
            )
            lives -= 1

    print(f"{' '.join(display)}")
    print(stages[lives])

    if lives <= 0:
        end_of_game = True
        print("You lose.")
    elif "_" not in display:
        end_of_game = True
        print("You win!")
