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
'''

#Write your code below this line 👇
import random

options = [rock, paper, scissors]

response = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

response_int = int(response)
if response_int >= 3 or response_int < 0:
  print("You typed an invalid number. You lose.")
else:
  print(options[response_int])

# if response_int == 0:
#   print(rock)
# elif response_int == 1:
#   print(paper)
# elif response_int == 2:
#   print(scissors)
# else:
#   print(None)

comp_response = random.randint(0,2)
print(f"Computer chose: {comp_response}")
print(options[comp_response])


# if comp_response == 0:
#   print(rock)
# if comp_response == 1:
#   print(paper)
# if comp_response ==2:
#   print(scissors)


if (response_int == 0 and comp_response == 2) or (response_int == 2 and comp_response == 1) or (response_int == 1 and comp_response == 0):  
  print("You win")
elif response_int == comp_response:
  print("There's a draw")
else:
  print("You lose")

'''

######## Angela's solution
import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number. You lose.")
else:
  print(game_images[user_choice])


  computer_choice = random.randint(0,2)
  print(f"Computer chose:")
  print(game_images[computer_choice])


  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif user_choice == computer_choice:
    print("It's a draw")
  else:
    print("You typed an invalid number. You lose.")





