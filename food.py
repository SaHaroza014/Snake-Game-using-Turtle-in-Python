from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape = 'circle'
        self.penup()
        self.shapesize(stretch_len=1.2, stretch_wid=1.2)
        self.color('red')
        self.speed('fastest')
        x_rand = random.choice(range(-280, 280))
        y_rand = random.choice(range(-280, 280))
        self.goto(x_rand, y_rand)
