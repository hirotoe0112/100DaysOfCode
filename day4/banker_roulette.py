import random
import names

names_split = names.names_string.split(", ")

name = names_split[random.randint(0, len(names_split) - 1)]

print(f"{name} is going to buy the meal today!")
