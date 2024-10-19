from turtle import _Screen

class Screen(_Screen):

    def __init__(self):
        super().__init__()
        self.setup(width=800, height=600)
        self.bgcolor("black")
        self.title("Pong")
        # self.tracer(0)
        # self.listen()
        # self.exitonclick()




