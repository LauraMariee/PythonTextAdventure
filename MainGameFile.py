from LootGenerator import *
from Enemy import *
from Dice import *
from Money import *
from Player import *
import sys

running = True
while running is True:
    choice = input("Do you want to roll, check the player status or open the inventory? \nChoice: ")
    if choice.upper() == "ROLL":
        diceRoll(player)
        movementCheck(player)
        print("\n")
        pass
    elif choice.upper() == "STATUS":
        itemType(item)
        playerStatus(player)
        print("\n")
    elif choice.upper() == "INVENTORY":
        openInventory()
        print("\n")
    elif choice.upper() == "EXIT":
        exit()
        pass




