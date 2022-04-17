######## Notes from lecture
# Conditional statement
'''
water level = 50
if water_level > 80:
  print("Drain water")
else:
  print("Continue")
'''

# Rollercoaster Tickets
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# age = int(input("What is your age?"))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    print("Your ticket is $5.")
#  elif age >= 12 and age <= 18:
#    print("You ticket is $7.")
  elif age<= 18:
    print("you ticket is $7.")
  else:
    print("Your ticket is $12.")
else:
  print("You do not meet the height requirement to ride the rollercoaster.")



'''
######## Exercise - Odd or Even Exercise
#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.
#The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
odd_or_even = number % 2

if odd_or_even == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
'''