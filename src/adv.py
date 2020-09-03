from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

### Notes about my code to make the game run ###
# My game starts with a welcome message, and explanation of the scenario, and asks the user if they would like to play. 
# If yes, It will run the functions I've written. 
# After the game, it will ask if you want to play again. If yes, run the functions again. If no, it will exit the game.

### Defining my functions ###
def display_intro():
    print("Welcome to the Great Treasure Hunt Adventure!")
    print()
    print("Princess Rosania needs your help. The evil usurper of her family's crown, Wart Drogo, has stolen mounds of gold and rubies from her family and hidden it away. If you help her find the treasure, you will be handsomely rewarded with a mound of gold of your own!")
    print()

def participate():
    answer = ""
    while answer.lower().strip() != "yes" and answer.lower().strip() != "no": #input validation
        answer = input("Would you like to help the princess find the treasure? (yes/no)")
    return answer
    if answer.lower().strip() == "yes":
        answer = input("Great! Let's get started. You are at a crossroads. Would you like to go north, south, east, or west?").lower().strip()
        if answer == "north":
            answer == input("You are now in the foyer. Would you like to go north, south, or east?").lower().strip()
    else:
        print("That's too bad!")

def greet_user(name):
    while True:
        if len(name) > 0:
            greeting = f"\nHello {name}! The princess is so happy to begin the adventure with you! Navigate to different rooms to find the hidden treasure. Good luck!\n"
            print(greeting)
            break
        else:
            print("Please provide an adventurer name")
            name = input("Type your name: \n>>  ")

# Make a new player object that is currently in the 'outside' room.
def start_game():
    player_name = input("Choose your player name: \n")
    greet_user(player_name)
    player = Player(player_name, room["outside"])


playAgain = "yes" 
while playAgain == "yes" or playAgain == "y":   
    display_intro()
    participate()
    start_game()
    #greet_user(player_name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
while True:
    print(f'You are currently in "{player.current_room.name}".')
    print(textwrap.dedent(player.current_room.description), '\n')
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")





# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

##TO DO:
# game is stuck in a loop. need to fix the loop first
# need to need to add the location identifier of which room they are in
# need to add ability to move into a different room