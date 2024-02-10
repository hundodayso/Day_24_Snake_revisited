from turtle import Screen, Turtle
import time
import random
from snake import Snake
from food import Food
from scoreboard import Score

SCREENW, SCREENH = 600, 600

# Setup
screen = Screen()
screen.setup(width=SCREENW, height=SCREENH)
screen.bgcolor('black')
screen.title("Snake Game!")
screen.colormode(255)
screen.tracer(0)
segments = []
rev_segments = []
game_on = True
colours = ["blue", "green", "red", "yellow"]

snake = Snake()
food = Food()
score = Score()
print(f"X: {food.random_x}, Y:{food.random_y}")

screen.listen()


screen.onkey(snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


while game_on:

    snake_length = len(segments)
    screen.update()
    time.sleep(0.1)

    #print(snake.head.xcor)

    #Detect collision with food
 #   print(f"HEAD: X: {round(snake.head.xcor())}, Y: {round(snake.head.ycor())}")
  #  print(f"FOOD:   X: {food.random_x}, Y:{food.random_y}")
    if round(snake.head.xcor()) == food.random_x and round(snake.head.ycor()) == food.random_y:
        snake.add_segment(food.random_x, food.random_y)
        food.refresh()
        game_score = score.get_score() + 1
        score.set_score(game_score)
    elif snake.check_tail():
        game_on = False
        score.game_over()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()


    snake.move()







screen.exitonclick()


