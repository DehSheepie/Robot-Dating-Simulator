from Biome import Biome
import random


class BiomeGen:
    def __init__(self):
        self.biomes = [Biome("Tropical", 3, "You got lost in the tropics."),
                       Biome("Aquatic", 5, "You were attacked be a sea creature."),
                       Biome("Metropolitan", 4, "You got lost."),
                       Biome("Desert", 1, "You got lost."), Biome("Desolate", 1, "You got bored and decided to leave."),
                       Biome("Forest", 5, "You lost your way."), Biome("Jungle", 10, "You were attacked by a gorilla."),
                       Biome("Cavernous", 6, "You were hit by a falling rock."),
                       Biome("Volcanic", 18, "You narrowly escaped an erupting volcano"),
                       Biome("Badlands", 12, "You were chased by a group of bandits on dirt bikes."),
                       Biome("War Zone", 13, "You narrowly avoided a stray nuclear warhead."),
                       Biome("Industrial", 6,
                             "You were forced to work and had to pretend to go on break in order to get "
                             "away."), Biome("Swamp", 3, "You got stuck in the swamps."),
                       Biome("Primal", 17, "You were chased by a terrifying four headed dinosaur."),
                       Biome("Radioactive", 7, "The radiation damaged your circuitry."),
                       Biome("Glade", 1, "You couldn't find what your were looking for."),
                       Biome("Moorland", 1,
                             "You forgot to set the parking break for the ship and had to stop it floating "
                             "away."), Biome("Marshland", 2, "You got dirty and had to clean off."),
                       Biome("Infested", 8, "You narrowly avoided a swarm of hungry ants."),
                       Biome("Grassy", 1, "You got bored and decided to leave.")]

    def generate_biome(self):
        array_len = len(self.biomes)
        index = random.randint(0, array_len - 1)
        biomes = self.biomes[index]
        del self.biomes[index]
        return biomes
