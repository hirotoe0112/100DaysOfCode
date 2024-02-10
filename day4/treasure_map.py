line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?

position_x_chars = ["A", "B", "C"]
position_x_char = position[0].upper()
position_x_index = position_x_chars.index(position_x_char)
position_y_index = int(position[1]) - 1
map[position_y_index][position_x_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
