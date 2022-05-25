from turtle import Turtle

COLORS = ["green", "yellow", "orange"]


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()

    def create_bricks(self):

        y = 100
        for color in COLORS:
            for row in range(2):
                x = -265
                y += 25
                while x < 300:

                    new_brick = Turtle("square")
                    new_brick.penup()
                    new_brick.shapesize(stretch_wid=1, stretch_len=3)
                    new_brick.color(color)
                    new_brick.goto(x, y)
                    self.all_bricks.append(new_brick)
                    x += 65
