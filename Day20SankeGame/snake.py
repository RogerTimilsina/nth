from turtle import Turtle


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# size of square is 20 x 20 so each segment of snake body should be shifted by -20 in x-axis,
# otherwise all 3 of the squares will be in the same pos so they stack up and only 1 square will be visible.
starting_pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in starting_pos:
            self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, pos):
        new_segment = Turtle('square')
        new_segment.speed(0)
        new_segment.penup()
        new_segment.goto(pos)
        new_segment.color('white')
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
