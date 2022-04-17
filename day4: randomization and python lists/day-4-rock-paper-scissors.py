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

#  List of choices
choices = [rock, paper, scissors]

# User/my input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(choices[user_choice])
  
  # Determine computer's random choice
  computer_random_choice = random.randint(0,2)
  computer_choice = choices[computer_random_choice]
  print(f"Computer chose: {computer_choice}")
  
  # Take user/my input and computer's input to determine who wins  
  if user_choice == computer_random_choice:
    print("It's a draw.")
  elif user_choice == 0 and computer_random_choice == 2:
    print("You win.")
  elif user_choice == 2 and computer_random_choice == 0:
    print("You lose.")
  elif user_choice > computer_random_choice:
    print("You win.")
  elif computer_random_choice > user_choice:
    print("You lose.")
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





