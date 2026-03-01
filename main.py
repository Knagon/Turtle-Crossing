import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.10)
    screen.update()
    car_manager.move_all()

    if random.randint(1,8) == 1:
        car_manager.create_cars()

    for car in car_manager.cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False


    finish = player.finish_line()
    if finish:
        scoreboard.next_level()
        car_manager.level_up()
        player.reset_position()

screen.exitonclick()
