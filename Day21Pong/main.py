import turtle
import paddle
import ball
import time

screen = turtle.Screen()
screen.setup(800, 600)
screen.colormode(255)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle1 = paddle.Paddle((-350, 0))
paddle2 = paddle.Paddle((350, 0))
ball = ball.Ball((0, 0))

screen.update()
screen.listen()
screen.onkeypress(paddle1.up, 'w')
screen.onkeypress(paddle1.down, 's')
screen.onkeypress(paddle2.up, 'Up')
screen.onkeypress(paddle2.down, 'Down')

is_gameon = True
while is_gameon:
    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with side wall and add score
    if ball.xcor() > 380:
        ball.reset()
    if ball.xcor() < -380:
        ball.reset()

    # detect collision with the paddle
    if (ball.distance(paddle1) < 50 and ball.xcor() < 340) or (ball.distance(paddle2) < 50 and ball.xcor() > - 340):
        ball.bounce_x()
    ball.move()
    screen.update()
    time.sleep(0.03)
