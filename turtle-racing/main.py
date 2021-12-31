from turtle import Turtle, Screen
from random import randint
colors = ["red", "green", "blue", "purple", "yellow", "brown"]
screen = Screen()
screen.setup(width=500, height=400)
num_turtles = 6
turtles = []

for i in range(num_turtles):
    turtle = Turtle('turtle')
    turtle.color(colors[i])
    turtles.append(turtle)


user_bet = screen.textinput(title="Your bet", prompt="Choose {}".format("/".join(colors)))


for i in range(num_turtles):
    turtles[i].penup()
    turtles[i].setpos(x=-230, y=-150 + 50 * i)


is_bet_on = bool(user_bet)
while is_bet_on:
    for turtle in turtles:
        turtle.forward(randint(0, 20))
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_bet_on = False
            break

if user_bet == winning_color:
    print("You win the game")
else:
    print("You lose")

screen.exitonclick()
