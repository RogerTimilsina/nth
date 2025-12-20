from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed(4)
        self.goto(position)
        # start moving upwards at the beginning (since xmove = ymove, tanA is 1 so the angle of the ball will be 45)
        # can put any value of xfactor and yfactor as of now
        self.xmove = 10  # x displacement
        self.ymove = 10  # y displacement

    def reset(self):
        self.goto(0,0)
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1  # same as self.ymove = -self.ymove

    def bounce_x(self):
        self.xmove *= -1