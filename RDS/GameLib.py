from Player import Player
from Planet import Planet
from Robot import Robot

import random


class Game:
    @staticmethod
    def get_gender(x):
        genders = ["Fembot", "Masbot", "Androbot", "Neutrabot"]
        if x == 1:
            return genders[0]
        elif x == 2:
            return genders[1]
        elif x == 3:
            return genders[2]
        elif x == 4:
            return genders[3]

    @staticmethod
    def get_colour(x):
        colours = ["Maroon", "Brown", "Olive", "Teal", "Navy", "Black", "Red", "Orange", "Yellow", "Lime", "Green",
                   "Cyan",
                   "Blue", "Purple", "Magenta", "Grey", "Pink", "Apricot", "Beige", "Mint", "Lavender", "White"]
        return colours[x - 1]

    def create_player(self):
        # This will start the game and set up the player object
        p_colour = None
        p_gender = None
        print("Welcome to Robot Dating Simulator! \n__________________________________")
        print("+--------+\n|  o   o |\n|   --   |\n+--------+")
        name = input("What is your name?")
        end_loop = False
        while not end_loop:
            print("What type of bot are you?")
            print(" Enter [1] for Fembot \n Enter [2] for Masbot \n Enter [3] for Androbot \n Enter [4] for Neutrabot")
            p_gender = input("Type here:")
            if str.isdigit(p_gender):
                p_gender = int(p_gender)
                if 0 < p_gender <= 4:
                    end_loop = True
                else:
                    print("Please enter a number from 1 to 4")
            else:
                print("Please enter a valid number")
        end_loop = False
        while not end_loop:
            print("What colour are you?")
            print(" Enter [1] for Maroon   Enter [2] for Brown   Enter [3] for Olive")
            print(" Enter [4] for Teal   Enter [5] for Navy   Enter [6] for Black")
            print(" Enter [7] for Red   Enter [8] for Orange   Enter [9] for Yellow")
            print(" Enter [10] for Lime   Enter [11] for Green   Enter [12] for Cyan")
            print(" Enter [13] for Blue   Enter [14] for Purple   Enter [15] for Magenta")
            print(" Enter [16] for Grey   Enter [17] for Pink   Enter [18] for Apricot")
            print(" Enter [19] for Beige   Enter [20] for Mint   Enter [21] for Lavender")
            print(" Enter [22] for White")
            p_colour = input("Type here:")
            if str.isdigit(p_colour):
                p_colour = int(p_colour)
                if 0 < p_colour <= 22:
                    end_loop = True
            else:
                print("Please enter a valid number")
        return Player(name, self.get_gender(p_gender), self.get_colour(p_colour))

    @staticmethod
    def start_message(player):
        # TODO: Come back to this section and allow this method to take a player and a list of planets
        print("Message from your dating advisor:")
        print("________________________________")
        print("\nSalutations " + player.name + "! \n \nI can see you are quite the fetching " + player.gender +
              ".\nThat splendid " + player.colour + " paint job you have on really suits you. "
                                                    "It looks almost brand spanking new!\nI'm sure you'll be quite"
                                                    " popular with the other bots...")
        print(
            "\nNow, about you finding a proper companion...\nMost bots really appreciate being given a gift here and "
            "there; and for a bot of your calibre, I’m sure that won’t be an issue.\nThe difficult part, however, "
            "is getting the right gifts to the right bot.")
        print(
            "\nOh yeah, there are the dates too... Those can be quite difficult as well. "
            "Just be yourself and you'll do fine. Or you could try being whoever you think your beloved "
            "would like you to be.\nWhichever works best for you.")
        print("\nGood luck " + player.name + " though I've no doubt you won't need it.")
        print("\nBest Regards\n\nAdvisory bot #" + str(random.randint(1000, 9999)))
        print("________________________________")

    def new_gifts(self, planets):
        for planet in planets:
            for biome in planet.biomes:
                biome.new_gift()

    def show_planets(self, planets):

        print("Reachable planets in this system:\n"
              f"|Planet Name: [{planets[0].name}] Biomes: ", end="")
        for biome in planets[0].biomes:
            print(f"[{biome.name}] ", end="")  # Shows the biomes within a planet
        print("|")
        print(f"|Planet Name: [{planets[1].name}] Biomes: ", end="")
        for biome in planets[1].biomes:
            print(f"[{biome.name}] ", end="")
        print("|")
        print(f"|Planet Name: [{planets[2].name}] Biomes: ", end="")
        for biome in planets[2].biomes:
            print(f"[{biome.name}] ", end="")
        print("|")

    def scan_planets(self, planets):
        valid_response = False
        while valid_response is False:
            response = input(
                "[1] Would you like to scan for gift types? \n[2] Or would you like to scan for gift values?\n")
            if str.isdigit(response):
                response_num = int(response)
                if response_num == 1:
                    valid_response = True
                    x = 1  # The number each planet will show as
                    for planet in planets:
                        print(f"[{x}] {planet.name} | Gift Types: ", end="")
                        for biome in planet.biomes:
                            print(f"[{biome.gift.type}] ", end="")
                        print("|")
                        x += 1

                elif response_num == 2:
                    valid_response = True
                    x = 1  # The number each planet will show as
                    for planet in planets:
                        print(f"[{x}] {planet.name} | Gift Values: ", end="")
                        for biome in planet.biomes:
                            print(f"[{biome.gift.value}] ", end="")
                        print("|")
                        x += 1
                else:
                    print("Please enter the number 1 or 2.")
            else:
                print("Please enter an integer.")

    def select_planet(self, planets):
        chosen_planet = None
        valid_input = False
        while valid_input is False:
            planet_selection = input("Which planet will you visit?")
            if str.isdigit(planet_selection):  # Checks the input is an integer
                planet_index = int(planet_selection)
                if 0 < planet_index < 4:  # Checks the selection is valid
                    planet_index = planet_index - 1
                    chosen_planet = planets[planet_index]
                    valid_input = True
                else:
                    print("Please enter an integer between 1 and 3.")

            else:
                print("Please enter an integer.")
        return chosen_planet

    def select_biome(self, planet):
        selected_biome = None
        print(f"|{planet.name}|")
        number_of_biomes = 1
        for biome in planet.biomes:
            print(f"[{number_of_biomes}] {biome.name} | Danger Rating: {biome.danger} | Gift: {biome.gift.name}")
            number_of_biomes += 1
        valid_response = False
        while valid_response is False:
            response = input("Which biome will you try to find a gift from?")
            if str.isdigit(response):
                response_num = int(response)
                if 1 <= response_num <= number_of_biomes:
                    selected_biome = planet.biomes[response_num - 1]
                    valid_response = True
                else:
                    if number_of_biomes == 1:
                        print(f"Please enter the number 1.")
                    else:
                        print(f"Please enter an integer between 1 and {number_of_biomes}")
            else:
                print("Please enter a valid integer.")
        return selected_biome

    def find_gift(self, biome, player):
        dice_roll = random.randint(1, 10)
        print("You attempt to find a gift.")
        if dice_roll <= player.difficulty_level:
            print(f"{biome.oops} You took {biome.danger} damage.")  # Prints message for when a gift isn't found
            player.health -= biome.danger
        else:
            print(f"You found a gift: {biome.gift.name}")
            player.inventory.append(biome.gift)

    def game_turn(self, player, planets):
        self.show_planets(planets)
        print("________________________________")
        self.scan_planets(planets)
        print("________________________________")
        planet = self.select_planet(planets)
        print("________________________________")
        biome = self.select_biome(planet)  # Allows the player to select a biome to find a gift from on the planet
        print("________________________________")
        self.find_gift(biome, player)  # Determines whether a gift was collected

    def give_gifts(self, player, robots):
        if len(player.inventory) == 0:
            print("You do not have any gifts.")
        else:
            print("________________________________")
            print(f"{player.name}, here are your matches: \n"
                  f"[1] Robot Name: [{robots[0].name}] Gender: [{robots[0].gender}] Colour: [{robots[0].colour}] "
                  f"Favorite Gift: [{robots[0].favorite_gift}] Affection: [{robots[0].affection}] \n"

                  f"[2] Robot Name: [{robots[1].name}] Gender: [{robots[1].gender}] Colour: [{robots[1].colour}] "
                  f"Favorite Gift: [{robots[1].favorite_gift}] Affection: [{robots[1].affection}] \n"

                  f"[3] Robot Name: [{robots[2].name}] Gender: [{robots[2].gender}] Colour: [{robots[2].colour}] "
                  f"Favorite Gift: [{robots[2].favorite_gift}] Affection: [{robots[2].affection}]")
            print("________________________________")
        robot_index = None
        gift_index = None
        valid_response = False
        while valid_response is False:
            response = input("Which Robot would you like to give a gift to?")
            if str.isdigit(response):
                if 0 < int(response) < 4:
                    robot_index = int(response) - 1
                    valid_response = True
                else:
                    print("Please enter an integer between 1 and 3.")
            else:
                print("Please enter a valid integer")

        print("Gifts:")
        selection_number = 1
        for gift in player.inventory:
            print(f"[{selection_number}] Name: [{gift.name}] Type: [{gift.type}] Value: [{gift.value}]")
            selection_number += 1

        valid_response = False
        while valid_response is False:
            response = input("Which Gift would you like to give?")
            if str.isdigit(response):
                if 0 < int(response) <= len(player.inventory):
                    gift_index = int(response) - 1
                    valid_response = True
                else:
                    print(f"Please enter an integer between 1 and {len(player.inventory)}.")
            else:
                print("Please enter a valid integer")

        self.calculate_affection(robots[robot_index], player.inventory[gift_index])

    def calculate_affection(self, robot, gift):
        if robot.favorite_gift == gift.name:
            robot.affection += 30
        elif robot.temperament == "Choleric":
            if gift.type == "Weapon":
                robot.affection += gift.value * 2  # Choleric bots like weapons
            elif gift.value < 7:
                robot.affection -= 11 - gift.value  # Choleric bots do not like cheap gifts
        elif robot.temperament == "Sanguine":
            if gift.type == "Upgrade":
                robot.affection += gift.value + 3  # Sanguine bots like upgrades
            elif gift.type == "Transport":
                robot.affection += gift.value - 10  # Sanguine bots don't like Transport gifts
            if gift.value > 7:
                robot.affection += gift.value * 2  # Sanguine bots like expensive gifts
        elif robot.temperament == "Phlegmatic":
            if gift.type == "Weapon":
                robot.affection -= gift.value  # Phlegmatic bots do not like Weapons
            if random.randint(1, 2) == 1:
                robot.affection += 5  # Phlegmatic bots sometimes just appreciate the fact a gift was given
        elif robot.temperament == "Melancholic":
            if gift.value > 7:
                robot.affection -= gift.value  # Melancholic bots do not like expensive gifts
            if random.randint(1, 5) == 1:
                robot.affection += 20  # Melancholic bots will sometimes jump up in affection after getting a gift
