from turtle import Turtle, Screen
class Paddle:
    def __init__(self, x_pos):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(x_pos, 0)
        self.paddle.setheading(90)


    def move_paddle_up(self):
        self.paddle.forward(20)

    def move_paddle_down(self):
        self.paddle.back(20)


