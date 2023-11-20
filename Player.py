from Dice import *
from LootGenerator import *
from Money import *
from Enemy import *

player = ["", "", 0, 50, False, 0]
# Name, Weapon, Level, Health, isDead, Position

def playerStatus(Player):
    print("The player is level", Player[2], "and has", Player[3], "health left.")
    print("The current weapon is a", item[1])
