import random

planets = ["Ladov", "Triaphus", "Nicutov", "Tongorth", "Mixicury", "Pauzuno", "Opra", "Zistroth", "Zeocury", "Govadus",
           "Braconia"]
descriptions = ["Tropical", "Aquatic", "Metropolitan", "Desert", "Desolate", "Forest", "Jungle", "Cavernous", "Volcanic"
    , "Badlands", "War Zone", "Industrial", "Swamp", "Primal", "Radioactive", "Glade", "Moorland"
    , "Marshland", "Infested", "Grassy"]


class Biomes:
    def __init__(self, name, danger, oops):
        self.name = name
        self.danger = danger
        self.oops = oops


class Player:
    def __init__(self, name, gender, colour):
        inventory = []
        self.name = name
        self.gender = gender
        self.colour = colour
        self.inventory = inventory


class Robot:
    def __init__(self, name, gender, colour, favorite_gift, temperament, bonus_gift):
        self.name = name
        self.gender = gender
        self.colour = colour
        self.f_gift = favorite_gift
        self.temperament = temperament
        self.b_gift = bonus_gift


class Planet:
    def __init__(self, name, description, common_gift, common_gift_chance):
        self.name = name
        self.description = description[0]
        self.gift = common_gift
        self.gift_chance = common_gift_chance


class Gift:
    def __init__(self, name, quality, is_special):
        self.name = name
        self.quality = quality
        self.is_special = is_special


def generate_biomes():
    biome = [Biomes("Tropical", 3, "You got lost in the tropics."),
             Biomes("Aquatic", 5, "You were attacked be a sea creature."), Biomes("Metropolitan", 4, "You got lost."),
             Biomes("Desert", 1, "You got lost."), Biomes("Desolate", 1, "You got bored and decided to leave."),
             Biomes("Forest", 5, "You lost your way."), Biomes("Jungle", 10, "You were attacked by a gorilla."),
             Biomes("Cavernous", 6, "You were hit by a falling rock."),
             Biomes("Volcanic", 18, "You narrowly escaped an erupting volcano"),
             Biomes("Badlands", 12, "You were chased by a group of bandits on dirt bikes."),
             Biomes("War Zone", 13, "You narrowly avoided a stray nuclear warhead."),
             Biomes("Industrial", 6, "You were forced to work and had to pretend to go on break in order to get "
                                     "away."), Biomes("Swamp", 3, "You got stuck in the swamps."),
             Biomes("Primal", 17, "You were chased by a terrifying four headed dinosaur."),
             Biomes("Radioactive", 7, "The radiation damaged your circuitry."),
             Biomes("Glade", 1, "You couldn't find what your were looking for."),
             Biomes("Moorland", 1, "You forgot to set the parking break for the ship and had to stop it floating "
                                   "away."), Biomes("Marshland", 2, "You got dirty and had to clean off."),
             Biomes("Infested", 8, "You narrowly avoided a swarm of hungry ants."),
             Biomes("Grassy", 1, "You got bored and decided to leave.")]
    return biome


def generate_gift():
    pass


def generate_planet():
    # Takes a planet name from the list and then removes that name from the pool
    global planets
    global descriptions
    n_planets = len(planets)
    planet = random.randint(0, n_planets - 1)
    name = planets[planet]
    list.remove(planets, planets[planet])
    print(name)
    # selects a random number of descriptors and removes each one from the pool after adding it
    biomes = generate_biomes()
    n = random.randint(1, 5)
    print(n)
    description = []
    while n >= 1:
        n_biomes = len(biomes)
        x = random.randint(0, n_biomes - 1)
        description.append(biomes[x])
        biomes.remove(biomes[x])
        n -= 1
    for b in description:
        print(b.name)
    danger = 0
    for b in description:
        danger += b.danger
    print("Danger: " + str(danger))
    return planet


def get_colour(x):
    colours = ["Maroon", "Brown", "Olive", "Teal", "Navy", "Black", "Red", "Orange", "Yellow", "Lime", "Green", "Cyan",
               "Blue", "Purple", "Magenta", "Grey", "Pink", "Apricot", "Beige", "Mint", "Lavender", "White"]
    return colours[x - 1]


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


def start_game():
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
    return Player(name, get_gender(p_gender), get_colour(p_colour),)


def game():
    # test area
    generate_planet()
    generate_planet()
    generate_planet()
    # player is the object that stores the player info

    player = start_game()
    print("Message from your dating advisor:")
    print("________________________________")
    print("\nSalutations " + player.name + "! \n \nI can see you are quite the fetching " + player.gender +
          ".\nThat splendid " + player.colour + " paint job you have on really suits you. "
          "It looks almost brand spanking new!\nI'm sure you'll be quite popular with the other bots...")
    print(
        "\nNow, about you finding a proper companion...\nMost bots really appreciate being given a gift here and there;"
        "and for a bot of your calibre, I’m sure that won’t be an issue.\nThe difficult part, however, is getting the "
        "right gifts to the right bot.")
    print(
        "\nOh yeah, there are the dates too... Those can be quite difficult as well. "
        "Just be yourself and you'll do fine. Or you could try being whoever you think your beloved "
        "would like you to be.\nWhichever works best for you.")
    print("\nGood luck " + player.name + " though I've no doubt you won't need it.")
    print("\nBest Regards\n\nAdvisory bot #" + str(random.randint(1000, 9999)))
    print("________________________________")


game()
