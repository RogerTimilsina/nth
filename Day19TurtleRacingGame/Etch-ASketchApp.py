import turtle as t


def move_forward():
    tim.forward(10)


def turn_left():
    tim.left(15)


def turn_right():
    tim.right(15)


def move_back():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def clear_w():
    tim.pencolor("white")
    tim.forward(10)
    tim.pendown()
    tim.pencolor("black")


tim = t.Turtle()
screen = t.Screen()

screen.listen()
screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=move_back, key="s")
screen.onkeypress(fun=clear, key="c")
screen.onkeypress(fun=clear_w, key="q")

screen.exitonclick()
