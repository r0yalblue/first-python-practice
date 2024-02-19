# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """Converts "rock", "paper", etc into a number"""
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: " + name + " is not a valid input."


def number_to_name(number):
    """Converts a number into "rock", "paper", etc"""
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: " + str(number) + " is not a valid input."

    
# main function

import random

def rpsls(player_choice): 
    """executes the game, prints out the player and computer choices and game outcome"""
    
# print player's choice and convert it to the appropriate number
    print(" ")
    print ("Player chooses " + player_choice)
    player_number = name_to_number(player_choice)

# compute random guess for computer and print it out
    comp_number = random.randrange(0, 5)
    print ("Computer chooses " + number_to_name(comp_number))
    
# calculate the winner and print the result

    diff_modulo_five = (comp_number - player_number) % 5
    if diff_modulo_five == 1 or diff_modulo_five == 2:
        print ("Computer wins!")
    elif diff_modulo_five == 3 or diff_modulo_five == 4:
        print ("Player wins!")
    elif diff_modulo_five == 0:
        print ("Player and computer tie!")
    else:
        print ("Error: could not calculate a winner.")
    
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


