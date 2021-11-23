## Rock Paper Scissors

# Instructions
'''
Make a rock, paper, scissors game. 

Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console. 

Start the game by asking the player:

*"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

From there you will need to figure out: 
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player. 

You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)


# Solution

[https://replit.com/@appbrewery/rock-paper-scissors-end](https://replit.com/@appbrewery/rock-paper-scissors-end)
'''
######## Exercise - Treasure Map
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Rock(0) wins against scissors(2).
# Scissors(2) win against paper(1).
# Paper(1) wins against rock(0).


#Write your code below this line 👇
import random

# choices = [rock, paper, scissors]
# choices[0]



response = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

response_int = int(response)
if response_int == 0:
  print(rock)
if response_int == 1:
  print(paper)
if response_int == 2:
  print(scissors)

comp_response = random.randint(0,2)
print(f"Computer chooses: {comp_response}")

if comp_response == 0:
  print(rock)
if comp_response == 1:
  print(paper)
if comp_response ==2:
  print(scissors)


if (response_int == 0 and comp_response == 2) or (response_int == 2 and comp_response == 1) or (response_int == 1 and comp_response == 0):  
  print("You win")
if response_int == comp_response:
  print("There's a draw")
else:
  print("You lose")