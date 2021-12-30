import turtle
import colorgram
from turtle import Turtle, Screen, colormode
from random import choice, randint


def draw_a_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_a_dashed_line(turtle):
    for i in range(10):
        turtle.forward(20)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()


def draw_shapes():
    colors = ["dark orange", "brown", "light salmon", "cyan", "medium blue", "powder blue", "lime", "yellow"]
    turtle = Turtle("turtle")
    shape_edges = {
        "triangle": 3,
        "square": 4,
        "pentagon": 5,
        "hexagon": 6,
        "heptagon": 7,
        "octagon": 8,
        "nonagon": 9,
        "decagon": 10
    }

    for edge in shape_edges.values():
        turtle.color(choice(colors))
        for i in range(edge):
            turtle.right(360 / edge)
            turtle.forward(100)


def draw_random():
    colormode(255)
    turtle = Turtle("turtle")
    turtle.pensize(20)
    directions = [0, 90, 180, 270]
    for i in range(50):
        turtle.color(gen_random_color())
        turtle.setheading(choice(directions))
        turtle.forward(50)


def gen_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_sinopharm():
    colormode(255)
    n = 100
    turtle = Turtle()
    turtle.speed("fastest")
    for i in range(n):
        turtle.color(gen_random_color())
        turtle.setheading(turtle.heading() + 360 / n)
        turtle.circle(100)


def extract_colors_from_image():
    rgb_colors= []
    colors = colorgram.extract('shadow_eminence.jpeg', 30)
    for color in colors:
        rgb_colors.append(color.rgb)
    return rgb_colors


def draw_dots():
    turtle = Turtle()
    colormode(255)
    rgb_colors = extract_colors_from_image()
    width = 10
    height = 10
    for i in range(height):
        turtle.setpos(0, 50 * i)
        for j in range(width):
            turtle.color(choice(rgb_colors))
            turtle.pendown()
            turtle.dot(20)
            turtle.penup()
            turtle.forward(50)


# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("coral")

# draw_a_square(timmy_the_turtle)
# draw_a_dashed_line(timmy_the_turtle)
# draw_shapes()
# draw_random()
# draw_sinopharm()
# extract_colors_from_image()
draw_dots()

screen = Screen()
screen.exitonclick()