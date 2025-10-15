from turtle import Turtle

class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=6, stretch_wid=2)
        
    

    def destroyBrick(self):
        self.hideturtle()
        self.clear()