__author__ = 'Les Pounder'

#The lines below imagicptsort modules of code into our game, in particular these imagicptsort time functions to allow us to pause and stop the game, and random provides a method of choosing random numbers or characters.
from time import *
from random import *
import json
import os,sys

#This is a function, we use it to do lots of things and then call it by it's name later on
#To create a function we use "def name():" where name can be anything.

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


def choose_direction():
    global move
    print ("To go north press n then enter")
    print ("To go east press e then enter")
    print ("To go west press w then enter")
    move = input("Which direction would you like to travel? ")
    if move == 'n':
        print (datastore["adventure"]["North"])
    #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
    elif move == 'e':
        print (datastore["adventure"]["East"])
    elif move == 'w':
        print (datastore["adventure"]["West"])
def carry_on():
    global hitpts
    global magicpts
    carryon = True

    if hitpts <= 0:
        carryon = False
        print("I am sorry hero, but all your health is spent!\nRest up and try again another time\n")
    elif len(datastore["adventure"]["NPCNames"]) == 0 and len(datastore["adventure"]["Enemies"]) == 0:
        carryon = False
        print("You have faced all your enemies, encountered all your friends, and lived to tell the tale!")
        print(name + ", you are the bravest hero in all of " + datastore["adventure"]["Kingdom"] + "!!!")
    return carryon

def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global hitpts
    global magicpts
    global datastore
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name hero? ")
    #open the adventure json database and read it into the datastore variable
    filename = "adventureDB.txt"
    if filename:
        with open(filename, 'r') as database:
            datastore = json.load(database)
    #randint is a great way of adding some variety to your players statistics.
    hitpts = randint(5,20)
    magicpts = randint(5,20)

def friend():
    #This will create a randomly named Friend to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = datastore["adventure"]["NPCResponses"]
    npcnamechoice = datastore["adventure"]["NPCNames"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice.pop()
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like some advice?\n")
    shuffle(responses)
    print ("Press y to talk to " + npcname)
    if input() == "y":
        print ("["+npcname+":] " +responses.pop() + "\n")
    else:
        print("["+npcname+":] Goodbye")

def enemy():
    global enemyhitpts
    global enemymagicpts
    global enemyname
    enemyhitpts = randint(5,20)
    enemymagicpts = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemies = datastore["adventure"]["Enemies"]
    shuffle(enemies)
    enemyname = enemies.pop()
    print("")
    print ("Suddenly you hear a commotion, and from the shadows you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print("")
    print ("Your enemy has " + " " + str(enemyhitpts) + " " + "Health Points")
    print ("Your enemy has " + " " + str(enemymagicpts) + " " + "Magic Points")
    print("")

def fight_enemy():
    global magicpts
    global hitpts
    global enemyname
    global enemyhitpts
    global enemymagicpts

    #The hero takes damage from the enemy but also causes damage, if she brought her sword
    hit = randint(0,magicpts)
    print ("You swing your sword and cause " + str(hit) + " of damage")
    enemyhitpts = enemyhitpts - hit
    print("Your enemy's hitpts = " + str(enemyhitpts))
    enemyhit = randint(0,enemymagicpts)
    print ("The " + enemyname + " swings a weapon at you and causes " + str(enemyhit) + " of damage")
    hitpts = hitpts - enemyhit
    print ("Your hitpts = " + str(hitpts))

def run_away():
    global enemyname
    global enemymagicpts
    global hitpts

    print ("You turn and run away from the " + enemyname)
    #the hero suffers damage if caught
    suffer = randint(0, 100)%2
    if suffer == 0:
        print("You escaped the clutches of the " + enemyname + "!")
    else:
        enemyhit = randint(0,enemymagicpts)
        print("You are caught by the enemy and suffer " + str(enemyhit) + " points of damage")
        hitpts = hitpts - enemyhit

    print ("Your hitpts = " + str(hitpts))

#We now use our functions in the game code, we call the title, the castle picture and then ask the game to run the setup for our character.
clear_screen()
title()
castle()
setup()
global name
global hitpts
global magicpts
global move
global enemyhitpts
global datastore
print ("Welcome to the land of " + datastore["adventure"]["Kingdom"] + ", "  + name)
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print ("\nYour health is" + " " + str(hitpts))
print ("Your magic skill is" + " " + str(magicpts))
sleep(2)
print ("")
print (datastore["adventure"]["StartingPlace"])

print ("")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":

    print ("Would you like to take your sword and shield?\nPress y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("sword")
        weapons.append("shield")
        print ("You are now carrying your " + weapons[0] + " and your" + " " + weapons[1])
    else:
        print ("You choose not to take your weapons")
    print ("You are ready to venture out into the land!")
else:
    print ("Nothing ventured, nothing gained!\nThe land of " + datastore["adventure"]["Kingdom"] + " is missing a hero.")
    print ("Game Over")
    sys.exit(0)

print (datastore["adventure"]["Destinations"])

#prompt the hero for a direction
print ("\n")
choose_direction()

#main game loops until we are out of enemy's and friends, or out of places to go
while carry_on():
    print("You are walking on your journey when...")
    #encounter a friend or enemy
    encounter = randint(0, 100)%2
    #if friend, choose to talk to them
    if encounter == 0 and len(datastore["adventure"]["NPCNames"]) > 0:
        print ("A friend is in your path and greets you\n")
        friend()

    #if enemy choose to fight or run
    elif len(datastore["adventure"]["Enemies"])> 0:
        enemy()
        print("You have " + str(hitpts) + " Health Points and " + str(magicpts) + " Magic Points\n")
        fight = input("Do you wish to fight?" )

        if fight == "y":
            fight_enemy()
        else:
            run_away()

    sleep(3)

print ("   _       _                 _")
print ("  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___")
print (" //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ ")
print ("/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/")
print ("\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|")

print ("                     _ _")
print ("  __ ___      ____ _(_) |_ ___")
print (" / _` \ \ /\ / / _` | | __/ __|")
print ("| (_| |\ V  V / (_| | | |_\__ \ ")
print (" \__,_| \_/\_/ \__,_|_|\__|___/")

print (" _   _  ___  _   _")
print ("| | | |/ _ \| | | |")
print ("| |_| | (_) | |_| |")
print (" \__, |\___/ \__,_|")
print (" |___/")
