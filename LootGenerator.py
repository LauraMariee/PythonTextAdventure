##########################################################
import random
from random import *
from decimal import Decimal
import math
##########################################################
#Array creation
item =["", '', 1, 0, 0, 0, 0, "", ""]
prefix = ["Warrior's", "Sage's", "Assassin's", "Jack's"]
suffix = ["Of the Bear", "Of the Fox", "Of chance"]
##########################################################
def prefixGenerator(Prefix, item):
    #print("PREFIX GENERATOR")
    prefixChoice = randrange(0, len(Prefix))#Get a random
    item[7] = Prefix[prefixChoice]
    if item[7] == "Warrior's":
        #print(str(prefixChoice))
        warrior(item)
    elif item[7] == "Sage's":
        mage(item)
    elif item[7] == "Assassin's":
        assassin(item)
    elif item[7] == "Jack's":
        jack(item)

def suffixGenerator(Suffix, item):
    #print("SUFFIX GENERATOR")
    suffixChoice = randrange(0, len(Suffix))
    item[8] = Suffix[suffixChoice]
    if item[8] == "Of the Bear":
        #print(str(suffixChoice))
        bear(item)
    elif item[8] == "Of the Fox":
        #print(str(suffixChoice))
        fox(item)
       # print("CHOICE 3")
    elif item[8] == "Of chance":
        #print(str(suffixChoice))
        chance(item)
        #print("CHOICE 3")

def set_name(item, Prefix, Suffix):
    #print("MODIFIER ADD")
    if item[2] == 0:
        #print("COMMON")
        rarity_name = "Common"
        print("The item is the", rarity_name,  item[0])
    elif item[2] == 1:
        #print("UNCOMMON")
        rarity_name = "Uncommon"
        prefixGenerator(Prefix, item)
        print("The item is the", rarity_name, item[7], item[0])
    elif item[2] == 2:
        #print("RARE")
        rarity_name = "Rare"
        prefixGenerator(Prefix, item)
        suffixGenerator(Suffix, item)
        print("The item is the", rarity_name, item[7], item[0], item[8])

def itemType(item):
    #print("ITEM TYPE")
    rarity_array = [0] * 80 + [1] * 15 + [2] * 5
    rarity = rarity_array[randrange(0, len(rarity_array))]
    newItem = int(randrange(0, 2))
    if newItem == 0:
        item[0] = "Sword"
        item[1] = 'sword'
        item[2] = rarity
        item[3] = int(randrange(2, 4))
        item[4] = int(randrange(8, 10))
        item[5] = int(randrange(2, 6))
        item[6] = int(randrange(0, 2))
    elif newItem == 1:
        item[0] = "Staff"
        item[1] = 'staff'
        item[2] = rarity
        item[3] = int(randrange(5, 6))
        item[4] = int(randrange(8, 10))
        item[5] = int(randrange(0, 2))
        item[6] = int(randrange(2, 6))


def status(Prefix, Suffix, item):
    #print("STATUS")
    set_name(item, Prefix, Suffix)
    print("The max damage is:", item[4])
    print("The min damage is:", item[3])
    print("The strength is:", item[5])
    print("The intelligence is:", item[6])
############################################################################################
def warrior(item):
   # print("CLASS WARRIOR")
    multiply = Decimal(uniform(1.5, 2.5))
    increase = int(randrange(1, 4))
    if item[5] == 0:
        item[5] += increase
        item[5] = math.floor(item[5])
    else:
        item[5] *= multiply
        item[5] = math.floor(item[5])

def mage(item):
   # print("CLASS MAGE")
    increase = int(randrange(1, 4))
    multiplier = float(uniform(1.5, 2.5))

    if item[6] == 0:
        item[6] += increase
    else:
        item[6] *= multiplier
        item[6] = math.floor(item[6])

def assassin(item):
   # print("CLASS ASASSAIN")
    increase = int(randrange(1, 3))
    item[3] += increase
    item[4] += increase

def jack(item):
    item[4] *= 1.5
    item[3] *= 1.5
    item[5] *= 1.5
    item[6] *= 1.5
    item[4] = math.floor(item[4])
    item[3] = math.floor(item[3])
    item[5] = math.floor(item[5])
    item[6] = math.floor(item[6])
#########################################################################################
def bear(item):
    item[5] *= 2
    item[5] = math.floor(item[5])

def fox(item):
    item[6] *=2
    item[6] = math.floor(item[6])

def chance(item):
    item[3] /= 2
    item[4] *= 2
    item[3] = math.floor(item[3])
    item[4] = math.floor(item[4])
