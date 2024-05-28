import pandas

csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_data = {row.letter: row.code for _, row in csv_data.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        result = [dict_data[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
