from turtle import Turtle, Screen

turtle = Turtle('turtle')
screen = Screen()


def move_forward():
    turtle.forward(20)


def move_backware():
    turtle.back(20)


def tilt_left():
    turtle.left(15)


def tilt_right():
    turtle.right(15)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backware)
screen.onkey(key="a", fun=tilt_left)
screen.onkey(key="d", fun=tilt_right)
screen.exitonclick()
