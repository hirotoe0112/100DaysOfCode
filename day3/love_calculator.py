print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?

T = 0
R = 0
U = 0
E = 0
L = 0
O = 0
V = 0

for char in name1 + name2:
    if char == "T" or char == "t":
        T += 1
    elif char == "R" or char == "r":
        R += 1
    elif char == "U" or char == "u":
        U += 1
    elif char == "E" or char == "e":
        E += 1
    elif char == "L" or char == "l":
        L += 1
    elif char == "O" or char == "o":
        O += 1
    elif char == "V" or char == "v":
        V += 1

score = int(str(T + R + U + E) + str(L + O + V + E))

if score < 10 or 90 < score:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
