######## Exercise - Leap Year
# Instructions

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

# [https://www.youtube.com/watch?v=xX96xng7sAE](https://www.youtube.com/watch?v=xX96xng7sAE)

# This is how you work out whether if a particular year is a leap year. 

# > on every year that is evenly divisible by 4
# >   **except** every year that is evenly divisible by 100
# >     **unless** the year is also evenly divisible by 400`

print("Welcome to Leap Year Determination!")
year = input("Input a yearWhich year do you want to check?\n")

if year % 4 !=:
  print("Not leap year")
elif