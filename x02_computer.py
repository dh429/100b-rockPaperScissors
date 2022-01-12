#!python3
from random import randint
import random
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""

def computerChoice():
  
  choice = randint(0,3)

  if choice == 0:
    value = "rock"
    return value
  if choice == 1:
    value = "paper"
    return value
  if choice == 2:
    value = "scissors"
    return value


if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
