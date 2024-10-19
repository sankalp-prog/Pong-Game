from turtle import Turtle 

MOVE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)

        

