# import colorgram
# extracted the colors and printed them in console using this code. Then copied the rgb values list from the console
# and pasted them in colors[]
# rgb_colors = []
# colors = colorgram.extract('paint.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)


import turtle as t
import random


def move_to_start_pos(tim):
    tim.setheading(225)
    tim.penup()
    tim.forward(350)
    tim.setheading(0)


def change_line(tim):
    tim.penup()
    tim.setheading(180)
    tim.forward(500)  # 50 * 10 = 500
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


colors = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129),
          (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23),
          (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41),
          (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173),
          (160, 209, 191), (67, 86, 23), (219, 206, 8)]
tim = t.Turtle()
tim.pensize(5)
tim.speed(0)
screen = t.Screen()
screen.colormode(255)

move_to_start_pos(tim)
for i in range(10):
    for j in range(10):
        # moves 50 steps in one iteration upto 10 iterations
        tim.dot(30, random.choice(colors))
        tim.penup()
        tim.forward(50)

    # change line
    change_line(tim)

screen.exitonclick()
