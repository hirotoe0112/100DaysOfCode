import turtle

t = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    t.forward(10)


def move_backwords():
    t.backward(10)


def counter_clockwise():
    t.setheading(t.heading() + 10)


def clockwise():
    t.setheading(t.heading() - 10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwords)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()
