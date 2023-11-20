from Dice import *
from LootGenerator import *
from Money import *

enemy = ["", False, 1, 0, 0]
        #Name, isDead, Level, XP, Health

def enemyStatus(Enemy):
    print("The", Enemy[0], "is level", Enemy[2], "and has", Enemy[4], "health left.")

def enemyLevel(Enemy):
    if Enemy[2] >= 1 and Enemy[2] <= 20:
        lowLevelEnemy(Enemy)
    elif Enemy[2] >= 21 and Enemy[2]<= 40:
        lowerLevelEnemy(Enemy)
    elif Enemy[2] >= 41 and Enemy[2]<= 60:
        mediumLevelEnemy(Enemy)
    elif Enemy[2] >= 61 and Enemy[2]<= 80:
        higherLevelEnemy(Enemy)
    elif Enemy[2] >= 81 and Enemy[2]<= 100:
        highestLevelEnemy(Enemy)
#######################################################
def lowLevelEnemy(Enemy):
    Enemy[0] = "Low Level Enemy"
    Enemy[3] = randrange(0, 11)
    Enemy[4] = 20
    enemyStatus(enemy)
def lowerLevelEnemy(Enemy):
    Enemy[0] = "Lower Level Enemy"
    Enemy[3] = randrange(0, 11)
    Enemy[4] = 40
    enemyStatus(enemy)
def mediumLevelEnemy(Enemy):
    Enemy[0] = "Medium Level Enemy"
    Enemy[3] = randrange(0, 11)
    Enemy[4] = 60
    enemyStatus(enemy)
def higherLevelEnemy(Enemy):
    Enemy[0] = "Higher Level Enemy"
    Enemy[3] = randrange(0, 11)
    Enemy[4] = 80
    enemyStatus(enemy)
def highestLevelEnemy(Enemy):
    Enemy[0] = "Highest Level Enemy"
    Enemy[3] = randrange(0, 11)
    Enemy[4] = 100
    enemyStatus(enemy)
######################################################


