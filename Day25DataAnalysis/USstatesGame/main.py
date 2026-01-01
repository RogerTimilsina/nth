import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

ans_state = turtle.textinput("Guess the state", "Enter another state's name:")


screen.exitonclick()
