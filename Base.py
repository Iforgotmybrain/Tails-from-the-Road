# Text game
import time


def rollintro ():
    print("In the beginning, there was nothing but this line of text")
    time.sleep(2)
    print ("But soon that changed, and the program began to develop")


def startingroomlightswitch ():
    lightswitch = ""
    while lightswitch != "north" and lightswitch != "east":
        lightswitch = input("Which way do you go?")
        if lightswitch == "north":
            hallway()
        elif lightswitch == "east":
           bathroom()
    return lightswitch


def hallway ():
    print("You enter a hallway with a doorway to your north and a staircase to your south")
    hallway = input("Which direction do you go?")
    if hallway in ["south", "South", "s", "S"]:
        entranceway()
    elif hallway == in["north", "North", "n", "N"]:
        bedroom()

def bedroom ():
    print("You enter what seems to be a bedroom")

def entranceway ():
    print("You head down the stairs and enter the entrance way")
    print("You see a kitchen to your west, a living area to your east, and a front door to your north")
    entrancewaydirection = input("Which way do you go?").lower()
    if entrancewaydirection == "north"
        #leads to front door


def bathroom ():
    while True:
        print("You enter a bathroom, you see a trunk on the floor and the doorway you entered to your west")
        bathroom = input("What do you do?")
        if bathroom in ["trunk", "Trunk", "Chest", "chest"]:
            print("You open the trunk and find a mysterious silicone sculpture")
            time.sleep(5)
        elif bathroom in ["west", "w", "West"]:
            print("You return to the dim room, you see a doorway to your north and the bathroom to your east")
            return startingroomlightswitch()


rollintro()

playername = input("What is your name? >")

print("Hello {}" .format(playername))
time.sleep(3)
print("You are about to embark on a hastily made journey involving animal people")
time.sleep(3)
print("I'm not sure of the details quite yet, since I'm basically writing this as I go.")
time.sleep(3)
print("I'm sure it will be a perfectly coded, well wrote, masterpiece")
time.sleep(3)

print("But first, you must create your character")
time.sleep(3)
print("Your options are a Wolf, Fox, Lion, or Dragon")
time.sleep(2)
playerclass = input("Which do you choose?")
if playerclass in ['Wolf', 'wolf']:
    print("You have choose to be a Wolf")
elif playerclass in ['Fox', 'fox']:
    print("You have choose to be a Fox")
elif playerclass in ['Lion', 'lion']:
    print("You have choose to be a Lion")
elif playerclass in ['Dragon', 'dragon']:
    print("You have choose to be a Dragon")
time.sleep(2)
print("With that out of the way, let's get started")
time.sleep (2)
print("You are in a dimly-lit room, you see a doorway to your north and to your east")
time.sleep(3)
startingroomlightswitch()