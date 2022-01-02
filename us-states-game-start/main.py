from turtle import Turtle, Screen
import pandas as pd

image_path = "blank_states_img.gif"
data_path = "50_states.csv"
turtle = Turtle()
screen = Screen()
correct_guessed_states = []
data = pd.read_csv(data_path)
print(data.head())

screen.addshape(image_path)
turtle.shape(image_path)

while (len(correct_guessed_states) < len(data)):
    if len(correct_guessed_states) == 0:
        title = "Guess the state"
    else:
        title = f"{len(correct_guessed_states)}/{len(data)} States Correct"
    answer_state = screen.textinput(title, prompt="What's another state's name").title()
    
    if answer_state == "Exit":
        break
    
    found_row = data[data["state"] == answer_state]
    if len(found_row) > 0 and answer_state not in correct_guessed_states:
        correct_guessed_states.append(answer_state)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.setpos(x=float(found_row.x), y=float(found_row.y))
        turtle.pendown()
        turtle.write(answer_state)

# Print missed states to csv
if len(correct_guessed_states) < len(data):
    updated_frame = data.set_index("state", inplace=False).drop(correct_guessed_states, inplace=False)
    updated_frame.to_csv("missed_states.csv")
screen.mainloop()