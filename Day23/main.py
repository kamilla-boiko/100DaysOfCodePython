import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("thistle1")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if any(car.distance(player) < 20 for car in car_manager.cars):
        game_is_on = False
        scoreboard.game_over()

    if player.is_at_finish():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_score()


screen.exitonclick()
