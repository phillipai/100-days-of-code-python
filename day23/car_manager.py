from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.starting_speed = STARTING_MOVE_DISTANCE
        self.increment = MOVE_INCREMENT

    def add_car(self):
        car_chance = random.randint(1, 6)
        if car_chance == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def increase_speed(self):
        self.starting_speed += self.increment

    def move_car(self):
        for car in self.cars:
            car.backward(self.starting_speed)
