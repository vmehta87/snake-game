from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('my snake game')
screen.tracer(0)

my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.right, 'Right')


game_on = True
while game_on:
    screen.update()
    time.sleep(0.15)
    my_snake.move()
    # if my_snake.head.position() == food.position():
    #     print('got it')
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        scoreboard.increase_score()

    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 \
            or my_snake.head.ycor() < -280:
        scoreboard.reset()
        my_snake.reset()

    # if my_snake.head in my_snake.segments[1:-1]:
    #     scoreboard.game_over()
    #     game_on = False
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.reset()
            my_snake.reset()
screen.exitonclick()
