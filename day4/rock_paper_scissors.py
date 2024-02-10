import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

arts = [rock, paper, scissors]
your_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
computer_choice = random.randint(0, 2)

if 0 <= your_choice <= 2:
    print(arts[your_choice])
    print("Computer chose:")
    print(arts[computer_choice])

    if your_choice == computer_choice:
        print("It's a draw.")
    else:
        if your_choice == 0 and computer_choice == 2:
            print("You win!")
        elif your_choice == 1 and computer_choice == 0:
            print("You win!")
        elif your_choice == 2 and computer_choice == 1:
            print("You win!")
        else:
            print("You lose.")
else:
    print("You typed an invalid number, you lose.")
