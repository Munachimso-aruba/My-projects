from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.initial_locations = [(0,0), (-20, 0 ), (-20, 0)]
        for _ in range(1, 4):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.shapesize(1)
            self.segments.append(turtle)
        for seg in range(0, 3):
            self.segments[seg].penup()
            self.segments[seg].goto(self.initial_locations[seg])

    def move_forward(self):
        self.segments[0].penup()
        self.segments[0].forward(20)
        for seg in range(len(self.segments)-1, 0, -1):
            self.segments[seg].penup()
            self.segments[seg].goto(self.segments[seg - 1].pos())

    def turn_left(self):
        if self.segments[0].heading() == 90.0 or 270.0 and self.segments[0].heading() != 0.0:
            self.segments[0].setheading(180)

    def turn_right(self):
        if self.segments[0].heading() == 90.0 or 270.0 and self.segments[0].heading() != 180.0:
            self.segments[0].setheading(0)

    def go_up(self):
        if self.segments[0].heading() == 0.0 or 180.0 and self.segments[0].heading() != 270.0:
            self.segments[0].setheading(90)

    def go_down(self):
        if self.segments[0].heading() == 0.0 or 180.0 and self.segments[0].heading() != 90.0:
            self.segments[0].setheading(270)

    def add_segment(self):
        x_cor_last_seg = self.segments[(len(self.segments)-1)].xcor()
        y_cor_last_seg = self.segments[(len(self.segments)-1)].xcor()
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.shapesize(1)
        turtle.goto(x=x_cor_last_seg-20, y=y_cor_last_seg)
        self.segments.append(turtle)

    def check_constraints(self):
        for seg in range(2, len(self.segments)):
            if self.segments[0].xcor() > 300\
                or self.segments[0].xcor() < -300 \
                    or self.segments[0].ycor() > 300 \
                    or self.segments[0].ycor() < -300 \
                    or self.segments[seg].distance(self.segments[0].pos()) < 16:
                for seg in self.segments:
                    seg.hideturtle()
                return True
            else:
                return False

