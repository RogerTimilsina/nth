import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv("50_states.csv")

states_list = df.state.to_list()
guessed_states = []
score = len(guessed_states)


def write_state():
    st_name = turtle.Turtle()
    st_name.penup()
    st_name.hideturtle()
    st_name.color('black')
    state = df[df.state == ans_state]
    state_x = state['x'].item()
    state_y = state['y'].item()
    st_name.goto(state_x, state_y)
    st_name.write(ans_state, font=("Arial", 8, "normal"))


while score < len(states_list):
    # get user ans and capitalize first letter using .title()
    ans_state = turtle.textinput("Guess the state",
                                 f"Score : {score}\n Enter another state's name:").title()
    if ans_state == "Exit":
        missing_states = [
            state for state in states_list if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        print(f"states to learn: {missing_states}")
        new_data.to_csv("states_to_learn.csv")
        break
    elif ans_state in states_list:
        write_state()
        guessed_states.append(ans_state)
        score = len(guessed_states)
