#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *



pChoice = playerChoice()

cChoice = randint(0,3)

def game(computer, player):
  if computer == player:
    print("Tie")
  if player == 0 and computer == 1:
    print("Computer used paper, you lose")
  if player == 0 and computer == 2:
    print("Computer used scissors, you win")
  if player == 1 and computer == 0:
    print("Computer used rock, you win")
  if player == 1 and computer == 2:
    print("Computer used scissors, you lose")
  if player == 2 and computer == 0:
    print("Computer used rock, you lose")
  if player == 2 and computer == 1:
    print("Computer used paper, you win")

if __name__ == "__main__":
  game(cChoice,pChoice)

