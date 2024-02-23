from turtle import Turtle, Screen
from prettytable import PrettyTable
import random

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row({"aaa", "bbb"})
table.align = "l"
print(table)


def forward(turtle, distance):
    turtle.forward(distance)


def left(turtle, angle):
    turtle.left(angle)


operations = {
    "forward": forward,
    "left": left,
}

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DeepPink1")

my_screen = Screen()
while True:
    distance = random.randint(5, 50)
    operation = random.choice(list(operations.keys()))
    operations[operation](timmy, distance)

# my_screen.exitonclick()
