from turtle import Turtle, Screen

jimmy = Turtle()
print(jimmy)
jimmy.shape("turtle")
jimmy.color("coral")
jimmy.forward(100)

current_screen = Screen()
print(current_screen.canvheight)
current_screen.exitonclick()