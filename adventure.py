__author__ = 'Les Pounder'

#The lines below imagicptsort modules of code into our game, in particular these imagicptsort time functions to allow us to pause and stop the game, and random provides a method of choosing random numbers or characters.
from time import *
from random import *
import json
import os,sys

#This is a function, we use it to do lots of things and then call it by it's name later on
#To create a function we use "def name():" where name can be anything.

############## FUNCTIONS
def clear_screen():  #Simple function that clears the screen
    os.system('cls' if os.name=='nt' else 'clear')

def title():
     print ("   __                           _          __                                  ")
     print ("  / /  ___  __ _  ___ _ __   __| |   ___  / _|   /\  /\___ _ __ ___   ___  ___ ")
     print (" / /  / _ \/ _` |/ _ \ '_ \ / _` |  / _ \| |_   / /_/ / _ \ '__/ _ \ / _ \/ __|")
     print ("/ /__|  __/ (_| |  __/ | | | (_| | | (_) |  _| / __  /  __/ | | (_) |  __/\__ \ ")
     print ("\____/\___|\__, |\___|_| |_|\__,_|  \___/|_|   \/ /_/ \___|_|  \___/ \___||___/")
def castle():

    print ("*                                 |>>>                    +        ")
    print ("+          *                      |                   *       +")
    print ("                    |>>>      _  _|_  _   *     |>>>		   ")
    print ("           *        |        |;| |;| |;|        |                 *")
    print ("     +          _  _|_  _    \\.    .  /    _  _|_  _       +")
    print (" *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|")
    print ("               \\..      /    ||:+++. |    \\.    .  /           *")
    print ("      +         \\.  ,  /     ||:+++  |     \\:  .  /")
    print ("                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *")
    print ("          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +")
    print ("                 ||+++ ||.    .     .      . ||+++.|   *")
    print ("+   *            ||: . ||:.     . .   .  ,   ||:   |               *")
    print ("         *       ||:   ||:  ,     +       .  ||: , |      +")
    print ("  *              ||:   ||:.     +++++      . ||:   |         *")
    print ("     +           ||:   ||.     +++++++  .    ||: . |    +")
    print ("           +     ||: . ||: ,   +++++++ .  .  ||:   |             +")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |        *")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |")


def welcome_hero():
    global name
    global hitpts
    global magicpts
    global weapons
    global datastore

    print ("Welcome to the land of " + datastore["adventure"]["Kingdom"] + ", "  + name)
    print()
    #Sleep is Python's way of pausing the game for a specified number of seconds
    sleep(2)
    #Below we are using the helper functions to join a string of text to an integer via the str() helper.
    print ("Your health is" + " " + str(hitpts))
    print ("Your magic skill is" + " " + str(magicpts))
    sleep(2)
    print ()
    print (datastore["adventure"]["StartingPlace"])

    #Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
    if input() == "y":
        print()
        print ("Would you like to take your sword and shield?\nPress y then enter to continue")
        if input() == "y":
            #This is a list, and it can store many items, and to do that we "append" items to the list.
            weapons = []
            weapons.append("sword")
            weapons.append("shield")
            print()
            print ("You are now carrying your " + weapons[0] + " and your" + " " + weapons[1] + ".")
        else:
            print()
            print ("You choose not to take your weapons")
        print ("You are ready to venture out into the land!")
    else:
        print()
        print ("Nothing ventured, nothing gained!\nThe land of " + datastore["adventure"]["Kingdom"] + " is missing a hero.")
        game_over()
        sys.exit(0)

def choose_direction():
    global move
    global directions
    global final
    directionFound = False

    destStr = "In the distance"
    for destination in directions:
        destStr += " to the "
        destStr += destination["Direction"]
        destStr += " you can see "
        destStr += destination["Place"]
        destStr += ","

    destStr = destStr[:-1]
    destStr += "."
    print(destStr)
    print()
    for direction in directions:
        dirStr = "To go " + direction["Direction"] + " type " + direction["Direction"][0] + " then enter"
        print(dirStr)

    print()
    move = input("Which direction would you like to travel?\n")

    for direction in directions:
        if direction["Direction"][0] == move:
            print(direction["Chosen"])
            final = direction["Final"]
            directionFound = True

    if not directionFound:
        print()
        print("Direction '" + move + "' is unknown. Please try again.")
        print()
        choose_direction()

def carry_on():
    global hitpts
    global magicpts
    global carryon
    global final

    if hitpts <= 0:
        carryon = False
        print("I am sorry hero, but all your health is spent! You will not reach your destination of " + final + ".")
        print("Rest up and try again another time!")
    elif len(datastore["adventure"]["NPCNames"]) == 0 and len(datastore["adventure"]["Enemies"]) == 0 and len(datastore["adventure"]["Trials"]) == 0:
        carryon = False
        print("You made it to " + final + "!")
        print("You have battled all your enemies, encountered all your friends, faced all your trials, and lived to tell the tale!")
        print(name + ", you are the bravest hero in all of " + datastore["adventure"]["Kingdom"] + "!!!")
    return carryon

def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global hitpts
    global magicpts
    global datastore
    global carryon
    global directions

    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name, hero? ")
    #open the adventure json database and read it into the datastore variable
    filename = "adventureDB.txt"
    if filename:
        with open(filename, 'r') as database:
            datastore = json.load(database)
    #randint is a great way of adding some variety to your players statistics.
    hitpts = randint(5,20)
    magicpts = randint(5,20)
    carryon = True
    directions = datastore["adventure"]["Destinations"]

def friend():
    #This will create a randomly named Friend to interact with
    global npcname
    global response
    global hitpts

    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = datastore["adventure"]["NPCResponses"]
    npcnamechoice = datastore["adventure"]["NPCNames"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice.pop()
    print ("A friend is in your path and greets you")
    print()
    print ("["+npcname+":] Hello, my name is "+npcname+", Would you like some advice?")
    shuffle(responses)
    print ("Press y to talk to " + npcname)
    if input() == "y":
        print ("["+npcname+":] " +responses.pop() + "\n")
        bonus = randint(5,20)
        print("Your friend gives you " + str(bonus) + " health")
        hitpts += bonus
        print_stats()
    else:
        print("["+npcname+":] Goodbye")

def enemy():
    global enemyhitpts
    global enemymagicpts
    global foe
    enemyhitpts = randint(5,20)
    enemymagicpts = randint(5,20)

    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemies = datastore["adventure"]["Enemies"]
    shuffle(enemies)
    foe= enemies.pop()
    print ("Suddenly you hear a commotion, and from the shadows you see " + foe["Article"] + " "+ foe["Name"] +" coming straight at you....")
    print()
    print ("Your enemy has " + str(enemyhitpts) + " health")
    print ("Your enemy has " + str(enemymagicpts) + " magic power")
    print()
    print_stats()
    fight = input("Do you wish to fight?\n")

    if fight == "y":
        fight_enemy()
    else:
        run_away()

def fight_enemy():
    global magicpts
    global hitpts
    global foe
    global enemyhitpts
    global enemymagicpts

    #The hero takes damage from the enemy but also causes damage, if she brought her sword
    hit = randint(0,magicpts)
    print()
    print ("You swing your sword and cause " + str(hit) + " damage")
    enemyhitpts -= hit
    print("Your enemy's hitpts = " + str(enemyhitpts))
    enemyhit = randint(0,enemymagicpts)
    print ("The " + foe["Name"] + " swings a weapon at you and causes " + str(enemyhit) + " damage")
    hitpts -= enemyhit
    print_stats()

def run_away():
    global foe
    global enemymagicpts
    global hitpts

    print()
    print ("You turn and run away from the " + foe["Name"])
    #the hero suffers damage if caught
    suffer = randint(0, 100)%2
    if suffer == 0:
        print("You escaped the clutches of the " + foe["Name"] + "!")
    else:
        enemyhit = randint(0,enemymagicpts)
        print("You are caught by the enemy and suffer " + str(enemyhit) + " points of damage")
        hitpts -= enemyhit

    print()
    print_stats()

def trial():
    global carryon
    global magicpts

    trials = datastore["adventure"]["Trials"]
    trial = trials.pop()
    print(trial["Trial"])
    if input() == "y":
        success = randint(0, 100)%2
        if(success == 1):
            print()
            print(trial["Success"])
            print("You have gained " + str(trial["Magic"]) + " magic for your trial.")
            magicpts += trial["Magic"]
            carryon = True
            print()
            print_stats()
        else:
            print()
            print(trial["Failure"])
            print()
            carryon = bool(trial["Continue"])

def print_stats():
    global magicpts
    global hitpts
    print("You have " + str(hitpts) + " health and " + str(magicpts) + " magic power\n")

def game_over():
    global carryon

    carryon = False
    print(" _____                        _____")
    print("|  __ \                      |  _  | ")
    print("| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ ")
    print("| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|")
    print("| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |   ")
    print(" \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   ")
    print()

########### END FUNCTIONS

#We now use our functions in the game code, we call the title, the castle picture and then ask the game to run the setup for our character.
clear_screen()
title()
castle()
setup()
welcome_hero()

print()
#prompt the hero for a direction
print ()
choose_direction()
print()

#main game loops until we are out of enemies, trials, and friends
while carry_on():
    #print("**********   You are walking on your journey when...   **********")
    #encounter a friend, trial, or enemy
    encounter = randint(0, 100)%3
    if encounter == 0 and len(datastore["adventure"]["NPCNames"]) > 0:
      friend()

    elif encounter==1 and len(datastore["adventure"]["Trials"]) > 0:
      trial()

    elif len(datastore["adventure"]["Enemies"])> 0:
      enemy()

    elif len(datastore["adventure"]["Trials"]) > 0:
      trial()

    elif len(datastore["adventure"]["NPCNames"]) > 0:
      friend()

    input("Enter to continue...")
    print()

#we are at the end of the game
print()
game_over()
print()
