import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkey(player.move, "w")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) <= 19:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 300:
        player.setpos(0, -280)
        car_manager.level_up()
        scoreboard.score_up()

screen.exitonclick()