import random


class Robot:
    def __init__(self, name, gender, colour, favorite_gift):
        self.name = name
        self.gender = gender
        self.colour = colour
        self.favorite_gift = favorite_gift
        self.affection = 0
        self.temperaments = ["Choleric", "Sanguine", "Phlegmatic", "Melancholic"]
        self.temperament = self.generate_temperament()

    def generate_temperament(self):
        index = random.randint(0, 3)
        return self.temperaments[index]
