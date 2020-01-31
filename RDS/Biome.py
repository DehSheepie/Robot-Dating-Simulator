from Gift import Gift
import random


def generate_gift():
    gifts = [Gift("Rocket Speeder", 6, "Transport"), Gift("Drillship", 8, "Transport"),
             Gift("Spearfish Hydrofoil", 7, "Transport"), Gift("Mech Walker", 10, "Transport"),
             Gift("Hyper Drill", 5, "Upgrade"), Gift("Laser Scalpel", 7, "Upgrade"),
             Gift("Nuclear Reactor", 6, "Upgrade"), Gift("Warp Launcher", 8, "Weapon"),
             Gift("Particle Rail", 9, "Weapon"), Gift("Rocket Chainsaw", 9, "Weapon")]
    number_of_gifts = len(gifts)
    index = random.randint(0, number_of_gifts - 1)  # Selects a random gift
    return gifts[index]


class Biome:
    def __init__(self, name, danger, oops):
        self.name = name
        self.danger = danger
        self.oops = oops
        self.gift = generate_gift()

    def new_gift(self):
        self.gift = generate_gift()
