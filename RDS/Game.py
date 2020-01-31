from GameLib import Game
from PlanetGen import PlanetGen
from RobotGen import RobotGen
from Player import Player
from Planet import Planet
from Robot import Robot
from Gift import Gift
import time

# TODO: Add private methods where appropriate in the classes

robot_generator = RobotGen()  # The robot generator
current_game = Game()
planet_generator = PlanetGen()  # The planet generator for this game
player = current_game.create_player()  # The player for this game
current_game.start_message(player)

robots = [robot_generator.generate_robot(), robot_generator.generate_robot(), robot_generator.generate_robot()]
planets = [planet_generator.generate_planet(), planet_generator.generate_planet(), planet_generator.generate_planet()]

running = True
score = 100


def check_if_game_won(bots):
    for bot in bots:
        if bot.affection >= 100:
            return True


def check_if_player_dead(p):
    if p.health < 0:
        return True


print("[1] Easy, [2] Medium, [3] Hard")
response = input("Choose your difficulty setting")
if str.isdigit(response):
    difficulty = int(response)
    if 0 < difficulty < 4:
        player.difficulty_level = difficulty
        score = score + difficulty**3

while running:
    current_game.new_gifts(planets)
    current_game.game_turn(player, planets)
    score -= 1
    valid_response = False
    while valid_response is False:
        response = input("Would you like to give your gifts now? \n[1] yes \n[2] no")
        if str.isdigit(response):
            valid_response = True
            if int(response) == 1:
                current_game.give_gifts(player, robots)
                score -= 5
        else:
            print("Please enter a valid integer.")

    if check_if_game_won(robots):
        print(f"Well done! You win! You scored {score} points.")
        running = False

    if check_if_player_dead(player):
        print(f"You took too much damage. You lose. Better luck next time!")
        running = False
time.sleep(5)








