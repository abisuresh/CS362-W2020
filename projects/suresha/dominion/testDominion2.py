# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:42:42 2015

@author: Abbi Devins-Suresh
January 15, 2020
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# number of curses and victory cards
numVictory = testUtility.getNumVictory(player_names)
numCurses = testUtility.getNumCurses(player_names)

# Define box
box = testUtility.getBoxes(numVictory)

supply_order = testUtility.orderSupplies()

# Pick 10 cards from box to be in the supply.
# The supply always has these cards
supply = testUtility.buildSupply(player_names, numVictory, numCurses)

# initialize the trash
trash = testUtility.initTrash()

# Costruct the Player objects
players = testUtility.makePlayers(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)