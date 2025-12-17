from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=585, height=585)
screen.bgcolor("black")
screen.title("Sarpo")
screen.tracer(0)

food = Food()

snake = Snake()
screen.update()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.add_segment, "/")
screen.onkey(screen.bye, "e")

game_over = False

while not game_over:
    time.sleep(0.15)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.update()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_over = True

    # Detect collision with its own tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_over = True
screen.exitonclick()
