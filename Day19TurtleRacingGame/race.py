import turtle as t
import random

is_race_on = True
screen = t.Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")

screen.title("Turtle Racing Game")
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
yaxis = [-200, -150, -100, -50, 0, 50, 100]
turtles = []
for i, color in enumerate(colors):
    turt = t.Turtle(shape="turtle")
    turt.turtlesize(1.3)
    turt.color(color)
    turt.penup()
# since height is 500 and width is 600 and the center of screen is (0,0) the x-axis is -300 to 300 and y: -250 to 250
    turt.goto(-260, yaxis[i])
    turtles.append(turt)

if user_bet:
    is_race_on = True

winner = ''
while is_race_on:
    for turtle in turtles:
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 240:
            is_race_on = False
            winner = turtle.color()[0]

if user_bet == winner:
    print("You win!")
else:
    print(f"You lose! {winner} wins!")
screen.exitonclick()
