import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

is_game_on = True
user_answers = []
while is_game_on:
    answer_state = screen.textinput(
        title=f"{len(user_answers)}/{len(data)} States Correct",
        prompt="What's another state's name?",
    )
    if answer_state == None:
        is_game_on = False
        break
    elif answer_state.title() in data.state.values:
        state = data[data.state == answer_state.title()]
        writer.goto(int(state.x), int(state.y))
        writer.write(answer_state.title(), align="center")
        user_answers.append(answer_state)

    if len(data) == len(user_answers):
        is_game_on = False
        break

missing_states = []
for state in data.state.to_list():
    if state not in user_answers:
        missing_states.append(state)
pandas.DataFrame(missing_states).to_csv(
    "states_to_learn.csv", index=False, header=False
)

screen.bye()
