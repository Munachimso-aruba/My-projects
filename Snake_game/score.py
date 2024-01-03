from turtle import Turtle
class Score:

    def __init__(self):
        self.score = 0
        self.score_writer = Turtle()
        self.score_writer.color("white")
        self.score_writer.hideturtle()
        self.score_writer.penup()
        self.score_writer.goto(0, 260)

    def update_score(self):
        self.score += 1
        self.score_writer.clear()
        self.score_writer.write(arg=f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))
