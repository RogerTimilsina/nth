from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.speed('fastest')
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as DATA:
            self.high_score = int(DATA.read())
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}\t High Score: {self.high_score}", False, "center", ("Comic Sans MS", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as DATA:
                DATA.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",False,"center", ("Comic Sans MS", 20, "normal"))
