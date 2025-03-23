import random

small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

class Character:
    def __init__(self):
        self.__combat_strength = random.choice(small_dice_options)
        self.__health_points = random.choice(big_dice_options)

    def __del__(self):
        print("This Character is being destroyed by the garbage collector!\n")

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, strength):
        if isinstance(strength, int) and strength >= 0:
            self.__combat_strength = strength
        else:
            print("Invalid combat strength.")

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, hp):
        if isinstance(hp, int) and hp >= 0:
            self.__health_points = hp
        else:
            print("Invalid health points.")
