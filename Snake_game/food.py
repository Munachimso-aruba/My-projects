from turtle import Turtle
import random as rd
class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.shapesize(0.5)
        self.food.color("blue")
        self.food.penup()

    def randomize_location(self):
        x_cor = rd.randint(-270, 270)
        y_cor = rd.randint(-270, 270)
        self.food.goto(x=x_cor, y=y_cor)
