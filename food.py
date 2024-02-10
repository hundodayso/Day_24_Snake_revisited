from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(self.colour_randomiser())
        self.speed("fastest")
        self.refresh()

    def colour_randomiser(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def refresh(self):
        self.random_x = random.randrange(-280, 280, 20)
        self.random_y = random.randrange(-280, 280, 20)
        self.color(self.colour_randomiser())
        self.setpos(self.random_x, self.random_y)
