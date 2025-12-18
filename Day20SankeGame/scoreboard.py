from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.speed(0)
        self.goto(0,270)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}",False,"center", ("Comic Sans MS", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center", ("Comic Sans MS", 20, "normal"))