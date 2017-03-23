# Script Name	: dice.py
# Author		: Craig Richards
# Created		: 05th February 2017
# Description	: This will randomly select two numbers, like throwing dice, you can change the sides of the dice if you wish

# Modifications	: Added functionality to choose number of dice and number of sides on those dice by system argument,
#               : if no arguments are passed then two six sided dice are rolled (as in original file)
# Last Modified	: 23rd March 2017
# Modified by   : Sam Kazar
# Version		: 2.0

import random
import sys

try:
    num_of_dice = int(sys.argv[1])
    num_of_sides = int(sys.argv[2])

except (IndexError, ValueError):
    num_of_dice = 2
    num_of_sides = 6

class Die(object):

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

for x in range(0, num_of_dice):
    print(Die(num_of_sides).roll())
