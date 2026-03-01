from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        rand_num = random.randint(1,4)
        for i in range(rand_num):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)


    def move_all(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

