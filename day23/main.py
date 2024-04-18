from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor(
    (random.randint(220, 255), random.randint(220, 255), random.randint(220, 255))
)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:

    # update cars
    car_manager.move_cars()
    if random.randint(1, 6) == 6:
        car_manager.create_car()
        create_car_counter = 0

    # detect collision with wall
    if player.ycor() > 280:
        scoreboard.level_up()
        car_manager.speed_up()
        player.reset()

    # detect collision with car
    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False

    screen.update()
    time.sleep(0.1)


screen.exitonclick()
