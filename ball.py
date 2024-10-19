from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10 
        self.y_move = 10
        self.move_speed = 0.1
        

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reverse_direction_and_speed_up(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def out_of_bounds(self):
            self.teleport(0,0)
            self.move_speed = 0.1 
            self.reverse_direction_and_speed_up()

