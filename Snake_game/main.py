from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
continue_game = True
screen = Screen()
screen.setup(width=600, height=600)
food = Food()
food.randomize_location()
screen.bgcolor("black")
snake = Snake()
score = Score()
screen.tracer(0)
while continue_game:
    snake.move_forward()
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.listen()
    if food.food.distance(snake.segments[0].pos()) < 16:
        score.update_score()
        food.randomize_location()
        snake.add_segment()

    if snake.check_constraints() == True:
        score.score = 0
        score.score_writer.clear()
        score.score_writer.write(arg=f"Score: {score.score}", align="center", font=('Arial', 24, 'normal'))
        snake = Snake()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()