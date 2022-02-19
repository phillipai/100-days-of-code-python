import turtle as t
import random
t.Turtle()

color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), (215, 69, 105), (98, 197, 234),
              (250, 51, 22), (203, 70, 21), (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166),
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), (20, 156, 51), (24, 36, 86), (252, 220, 0),
              (164, 28, 8), (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), (254, 12, 3), (38, 48, 98),
              (98, 96, 186)]

random_color = (random.choice(color_list))
t.colormode(255)
t.penup()
t.speed("fastest")
t.hideturtle()


def left_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(0)


def right_up():
    t.setheading(90)
    t.forward(50)
    t.setheading(180)


for _ in range(5):
    for _ in range(10):
        t.dot(20, (random.choice(color_list)))
        t.setheading(180)
        t.forward(50)
    left_up()
    for _ in range(10):
        t.forward(50)
        t.dot(20, (random.choice(color_list)))
    right_up()


screen = t.Screen()
screen.exitonclick()
