from racing_turtle import RacingTurtle
from turtle import Screen
from tkinter import messagebox

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

textinput_message = "Which turtle will win the race? Enter a color: " + ", ".join(
    colors
)
user_choice = screen.textinput("Make your bet", textinput_message)
while user_choice not in colors and user_choice is not None:
    user_choice = screen.textinput("Make your bet", textinput_message)

if user_choice is None:
    screen.bye()
    exit()

turtles = []
for color in colors:
    y_axis = colors.index(color) * 30 - 70
    turtles.append(RacingTurtle(color, y_axis))

while True:
    for turtle in turtles:
        turtle.run()
    for turtle in turtles:
        if turtle.is_goal():
            winning_color = turtle.t.pencolor()
            if winning_color == user_choice:
                messagebox.showinfo(
                    "result", f"You've won! The {winning_color} turtle is the winner!"
                )
            else:
                messagebox.showinfo(
                    "result", f"You've lost! The {winning_color} turtle is the winner!"
                )
            screen.bye()
            exit()
