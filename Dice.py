from random import *
from LootGenerator import *
from Enemy import *
from Money import *
total = 0
inventory = []
activeSpot = 0

def diceRoll(Player):
    dice1 = randrange(0, 7)
    dice2 = randrange(0, 7)
    total = dice1 + dice2

    if dice1 == dice2:
        print("You rolled a double! Roll again!\n")
        dice1 = randrange(0, 7)
        dice2 = randrange(0, 7)
    if total > 1:
        print("The first dice rolled a" , dice1, "and the second dice rolled a" , dice2)
        print("You can move", total, "spaces!")
        print("\n")
    else:
        print("The first dice rolled a", dice1, "and the second dice rolled a", dice2)
        print("You can move", total, "space!")
    Player[5] += total
    print("The player is now at square", Player[5])
    print("\n")

def movementCheck(Player):
    global activeSpot
    activeSpot = (randrange(Player[5], Player[5]+1))
    if Player[5] == activeSpot:
        itemType(item)
        status(prefix, suffix, item)
        print("Treasure added to Inventory")
        addToInventory(Player)
    else:
        pass
    pass

def addToInventory(Player):
    global activeSpot
    if Player[5] == activeSpot:
        inventory.append(item[0])
        pass

def openInventory():
    #print("Item: ", inventory[0])#show general item
    for x in inventory:
        print("Item:", x)
    pass

