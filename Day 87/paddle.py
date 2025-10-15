from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=6, stretch_wid=2)
        self.penup()
        self.goto(0, -300)

    def moveLeft(self):
        self.backward(50)

    def moveRight(self):
        self.forward(50)


    