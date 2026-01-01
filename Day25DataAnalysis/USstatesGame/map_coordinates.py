# get the coordinates of US states from the given screen(of given US states image size)then save it to a file
# The file is named state_coordinates.txt in the format: state,x,y
# Reminder : the image is 725px by 491px size and centered at (0,0) in turtle screen
# if not centered properly, the coordinates will be off by some value
import turtle


def get_mouse_click_coor(x, y):
    state = turtle.textinput("Click Detected", "What's the state name?")
    with open('state_coordinates.txt', 'a') as f:
        f.write(f"{state},{x},{y}\n")


screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=600)

with open('state_coordinates.txt', 'w') as file:
    file.write("state,x,y\n")  # write header

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# after running this code, click on each state on the turtle screen to get its coordinates
# and enter the state name in the prompt that appears.
# The coordinates along with the state name will be saved in state_coordinates.txt file.
