######## Notes from lecture
'''
Random module: https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

You can import a module to use in your code

import random 
random_integer = random.randint(1,10)
print(random_interger)

randon_float = random.random()

random_decimal = random.randon() * 5

love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")
'''

'''
######## Exercise - Head or Tails
# Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails 
'''
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

random_side = random.randint(0,1)
if random_number == 0:
  print("Tails")
else:
  print("Heads")



