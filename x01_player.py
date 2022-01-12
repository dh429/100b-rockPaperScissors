#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  choice = input("Enter your choice")
  if choice == "rock":
    value = 0
    return value
  if choice == "paper":
    value = 1
    return value
  if choice == "scissors":
    value = 2
    return value
  


if __name__ == "__main__":
  player = playerChoice()
  print(player)
