from turtle import Turtle, Screen
import time
from snake import Snake

# display screen
my_screen = Screen()
my_screen.title('Snake Game')
my_screen.setup(width=1000, height=1000)  # screen size
my_screen.tracer(0)  # turn off tracer
my_screen.bgcolor('black')


snake = Snake()

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
my_screen.exitonclick()
