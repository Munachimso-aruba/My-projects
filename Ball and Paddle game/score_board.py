from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.update_score()

    def update_score(self):
        self.goto(100, 195)
        self.write(arg=f"{self.right_paddle_score}", font=("Arial", 80, "normal"))
        self.goto(-150, 195)
        self.write(arg=f"{self.left_paddle_score}", font=("Arial", 80, "normal"))

    def increase_left_paddle__score(self):
        self.left_paddle_score += 1
        self.clear()
        self.update_score()

    def increase_right_paddle__score(self):
        self.right_paddle_score += 1
        self.clear()
        self.update_score()

    def create_center_line(self):
        center_line = Turtle()
        center_line.color("white")
        center_line.speed("fastest")
        center_line.hideturtle()
        center_line.penup()
        center_line.goto(0, 280)
        center_line.setheading(270)
        for _ in range(40):
            center_line.pendown()
            center_line.forward(10)
            center_line.penup()
            center_line.forward(5)
