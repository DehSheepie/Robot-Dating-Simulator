from Robot import Robot
import random


class RobotGen:
    def __init__(self):
        self.robot_names = ["Golem", "Sark", "Spanner", "Twitch", "Spark", "Data", "Logic", "Lexi", "Bot 223",
                            "Bot 242", "Bot 233", "Berty"]
        self.genders = ["Fembot", "Masbot", "Androbot", "Neutrabot"]
        self.colours = ["Maroon", "Brown", "Olive", "Teal", "Navy", "Black", "Red", "Orange", "Yellow", "Lime", "Green",
                        "Cyan", "Blue", "Purple", "Magenta", "Grey", "Pink", "Apricot", "Beige",
                        "Mint", "Lavender", "White"]
        self.favorite_gifts = ["Rocket Speeder", "Drillship", "Spearfish Hydrofoil", "Mech Walker",
                                     "Hyper Drill", "Laser Scalpel", "Nuclear Reactor", "Warp Launcher",
                                     "Particle Rail", "Rocket Chainsaw"]

    def generate_robot(self):
        len_robot_names = len(self.robot_names)
        len_genders = len(self.genders)
        len_colours = len(self.colours)
        len_preferred_gift_types = len(self.favorite_gifts)

        i_robot_name = random.randint(0, len_robot_names - 1)  # "i" stands for index
        i_gender = random.randint(0, len_genders - 1)
        i_colour = random.randint(0, len_colours - 1)
        i_preferred_gift_type = random.randint(0, len_preferred_gift_types - 1)
        robot = Robot(self.robot_names[i_robot_name], self.genders[i_gender],
                      self.colours[i_colour], self.favorite_gifts[i_preferred_gift_type])
        del self.robot_names[i_robot_name]  # Removes the name of the bot from the pool to prevent duplicate named bots
        return robot
