from turtle import Turtle, Screen
from paddle_class import Paddle
from ball_class import Ball
import time
from score_board import ScoreBoard
screen = Screen()
screen.tracer(0)

left_paddle = Paddle(x_pos=-390)
right_paddle = Paddle(x_pos=385)

ball = Ball()

scoreboard = ScoreBoard()

screen.setup(width=800, height=600)
screen.bgcolor("blue")
screen.listen()
screen.onkeypress(fun=left_paddle.move_paddle_up, key="w")
screen.onkeypress(fun=left_paddle.move_paddle_down, key="a")
screen.onkeypress(fun=right_paddle.move_paddle_up, key="Up")
screen.onkeypress(fun=right_paddle.move_paddle_down, key="Down")
continue_game = True

scoreboard.create_center_line()

while continue_game:
    time.sleep(0.2)
    screen.update()

    # detect collision with top and bottom screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #     detect collision of ball with right paddle
    if ball.distance(right_paddle.paddle.xcor(), right_paddle.paddle.ycor()) < 50 \
            and ball.xcor() > 350:
        ball.x_move *= -1

    #     detect collision of ball with left paddle
    if ball.distance(left_paddle.paddle.xcor(), left_paddle.paddle.ycor()) < 50 \
            and ball.xcor() < -350:
        ball.x_move *= -1

    #  detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_paddle__score()

    #     detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_paddle__score()
    ball.move()
screen.exitonclick()
