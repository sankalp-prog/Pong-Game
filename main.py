from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

end_of_game = False
while not end_of_game:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.reverse_direction_and_speed_up()
    if ball.xcor() > 380: 
        scoreboard.give_point_to_left_user()
        ball.out_of_bounds()
    elif ball.xcor() < -380:
        scoreboard.give_point_to_right_user()
        ball.out_of_bounds()
    screen.update()

screen.exitonclick()