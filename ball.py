from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=10, stretch_wid=10)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-350, 350)
        self.goto(random_x, random_y)
