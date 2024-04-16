from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while True:
    ball.move()
    screen.update()
    time.sleep(ball.ball_speed)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(x_bounce=False)

    # Detect collision with paddles
    if (
        (340 > ball.xcor() > 320)
        and (r_paddle.ycor() + 60 > ball.ycor() > r_paddle.ycor() - 60)
    ) or (
        (-340 < ball.xcor() < -320)
        and (l_paddle.ycor() + 60 > ball.ycor() > l_paddle.ycor() - 60)
    ):
        ball.bounce(x_bounce=True)
        ball.speed_up()

    # Detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        ball.reset()
    # Detect L paddle misses
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        ball.reset()

screen.exitonclick()
