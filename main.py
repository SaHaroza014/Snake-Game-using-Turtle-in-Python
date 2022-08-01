import random
import turtle
from turtle import Screen
import time
from scoreboard import Score
from snake import Snake
from food import Food
from playsound import playsound

# display screen
my_screen = Screen()
my_screen.title('Snake Game')
my_screen.setup(width=600, height=600)  # screen size
my_screen.tracer(0)  # turn off tracer
my_screen.bgcolor('black')

score = Score()
snake = Snake()
food = Food()

my_screen.listen()
my_screen.onkey(snake.up, 'w')
my_screen.onkey(snake.down, 's')
my_screen.onkey(snake.left, 'a')
my_screen.onkey(snake.right, 'd')

game_on = True
while game_on:
    my_screen.update()  # moves as a piece
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        # playsound('beep.wav') # play 'beep' sound effect
        food.x_rand = random.choice(range(-280, 280))
        food.y_rand = random.choice(range(-280, 280))
        food.goto(food.x_rand, food.y_rand)
        snake.extend_snake()
        score.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -280:
        score.end_game()
        game_on = False

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_on = False
            score.end_game()
my_screen.exitonclick()
