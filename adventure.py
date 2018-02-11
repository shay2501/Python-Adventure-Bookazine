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

def north():
    print ("To go north press n then enter")
def east():
    print ("To go east press e then enter")
def south():
    print ("to go south press s then enter")
def west():
    print ("To go west press w then enter")


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global hitpts
    global magicpts
    global datastore
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = input("What is your name warrior? ")
    #open the adventure json database and read it into the datastore variable
    filename = "adventureDB.txt"
    if filename:
        with open(filename, 'r') as database:
            datastore = json.load(database)
    #randint is a great way of adding some variety to your players statistics.
    hitpts = randint(5,20)
    magicpts = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
    npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
    shuffle(responses)
    print ("Press y to talk to the villager")
    if input() == "y":
        print ("["+npcname+":] " +responses[0])
    else:
        print("["+npcname+":] Goodbye")

def enemy():
    global enemyhitpts
    global enemymagicpts
    global enemyname
    enemyhitpts = randint(5,20)
    enemymagicpts = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "Ogre"
    print ("\nSuddenly you hear a roar, and from the shadows you see an "+enemyname+" coming straight at you....")
    #print enemyname
    print ("Your enemy has " + " " + str(enemyhitpts) + " " + "Health Points")
    print ("Your enemy has " + " " + str(enemymagicpts) + " " + "Magic Points")


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



print ("Would you like to venture out into the land? Press y then enter to continue")
#Below we use input to ask for user input, and if it is equal to y, then the code underneath is run.
if input() == "y":
    print ("You are in your home, with a roaring fireplace in front of you, above the fire you can see your sword and shield")
    print ("Would you like to take your sword and shield? Press y then enter to continue")
    if input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("sword")
        weapons.append("shield")
        print ("You are now carrying your " + weapons[0] + " and your" + " " + weapons[1])
        print ("Armed with your " + weapons[0] + " and " + weapons[1] + " you swing open the door to your home and see a green valley gleaming in the sunshine.")
    else:
        print ("You choose not to take your weapons")
        print ("Armed with your sense of humour, You swing open the door to see a green valley full of opportunity awaiting you.")
else:
    print ("You stay at home, sat in your favourite chair watching the fire grow colder. The land of Narule no longer has a hero.")
    print ("Game Over")
    sys.exit(0)

print ("In the distance to the north you can see a small village, to the east you can see a river and to the west a field of wild flowers.")

#Remember those functions we created at the start of the code? Well here we are using them in the game.
print ("\n")
north()
east()
west()
move = input("Where would you like to go? ")
if move == 'n':
    print ("\nYou move to the north, walking in the sunshine.")
    print ("A villager is in your path and greets you")
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print ("\nYou walk to the river which lies to the east of your home.")
    print ("A villager is in your path and greets you")
elif move == 'w':
    print ("\nYou walk to the field of wild flowers, stopping to take in the beauty")
    print ("A villager is in your path and greets you\n")

villager()
enemy()
sleep(3)

fight = input("Do you wish to fight?" )

if fight == "y":
    while hitpts > 0:
#This loop will only work while our characters hitpts is greater than 0.
        hit = randint(0,5)
        print ("You swing your sword and cause " + str(hit) + " of damage")
        enemyhitpts = enemyhitpts - hit
        print(enemyhitpts)
        enemyhit = randint(0,5)
        print ("The ogre swings a club at you and causes " + str(enemyhit) + " of damage")
        hitpts = hitpts - enemyhit
        print (hitpts)
else:
    print ("You turn and run away from the ogre")

print ("This is where this temagicptslate ends, this is now YOUR world, build your adventure and share it with the world")

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
