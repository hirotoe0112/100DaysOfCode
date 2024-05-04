import pandas

csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_data = {row.letter: row.code for index, row in csv_data.iterrows()}

user_input = input("Enter a word: ").upper()
result = [dict_data[letter] for letter in user_input]
print(result)
