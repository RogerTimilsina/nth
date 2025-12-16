from turtle import Screen, Turtle
import random


# def draw_shape(side):
#     theta = 360/side
#     for _ in range(side):
#         color = random.choice(colors)
#         my_turtle.color(color)
#         print(color)
#         my_turtle.forward(50)
#         my_turtle.left(theta)


tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
tim.speed(0)
tim.pensize(7)

for i in range(100):
    tim.forward(30)
    tim.color(random_color())
    dirn = random.choice(direction)
    tim.setheading(dirn)

screen.exitonclick()

