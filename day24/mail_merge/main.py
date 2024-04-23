with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    letter = starting_letter_file.read()
    with open("./Input/Names/invited_names.txt") as invited_names_file:
        names = invited_names_file.read().splitlines()
        for name in names:
            letter_replaced = letter.replace("[name]", name)
            open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w").write(
                letter_replaced
            )
