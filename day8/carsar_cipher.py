from carsar_cipher_art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(logo)


def caesar(text, shift_amount, direction):
    return_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in text:
        if char in alphabet:
            current_index = alphabet.index(char)
            new_index = current_index + shift_amount
            return_text += alphabet[new_index]
        else:
            return_text += char
    print(f"The {direction}d text is {return_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    formatted_shift = shift % len(alphabet)

    caesar(text=text, shift_amount=formatted_shift, direction=direction)

    willing = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()
    if willing == "no":
        should_continue = False

print("Goodbye")
