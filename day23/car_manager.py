from turtle import Turtle
import random

starting_move_distance = 5
move_distace_increment = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = starting_move_distance

    def create_car(self):
        new_car = Turtle()
        new_car.color(
            (random.randint(0, 170), random.randint(0, 170), random.randint(0, 170))
        )
        new_car.penup()
        new_car.goto((300, random.randint(-250, 250)))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.goto((car.xcor() - self.move_distance, car.ycor()))
            if car.xcor() > 300:
                self.cars.remove(car)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def speed_up(self):
        self.move_distance += move_distace_increment
