# script description :Roll dice.
# function without return
from random import randint,uniform
import os
def RollDice():
    die1= randint(1,6)
    die2= randint(1,6)
    print(f"Die 1:{die1}")
    print(f"Die 2:{die2}")

#main
RollDice()
