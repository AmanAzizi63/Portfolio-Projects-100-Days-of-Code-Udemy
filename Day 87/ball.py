from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(2,2)

    def firstMove(self):
        self.goto(0, -300)


        