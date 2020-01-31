from Biome import Biome
from Planet import Planet
from BiomeGen import BiomeGen
import random

class PlanetGen:
    def __init__(self):
        self.planet_names = ["Ladov", "Triaphus", "Nicutov", "Tongorth", "Mixicury", "Pauzuno", "Opra", "Zistroth",
                             "Zeocury", "Govadus", "Braconia"]

    def generate_planet(self):
        array_len = len(self.planet_names)
        index = random.randint(0, array_len - 1)
        planet_name = self.planet_names[index]
        del self.planet_names[index]  # Removes the used name from the pool
        biome_generator = BiomeGen()
        number_of_biomes = random.randint(1, 5)
        biomes = []
        while number_of_biomes >= 1:
            biomes.append(biome_generator.generate_biome())  # Adds another biome to the array
            number_of_biomes -= 1
        planet = Planet(planet_name, biomes)
        return planet
