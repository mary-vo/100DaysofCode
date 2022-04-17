######## Notes from lecture
'''
# For loop with Range
for number in range (1,11,3):
  print(number)

# Add numbers from 1 - 100, using sum function and range:
print(sum(range(1,101)))

# Add numbers from 1 - 100, using sum function and range, with a loop:
l=[]
for number in range (1,101):
  l.append(number)
print(sum(l))

# Add numbers from 1 - 100, using range and for loop:
total = 0
for number in range (1,101):
  total += number
print(total)
'''

######## Exercise - Adding Evens
# Instructions
'''
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Hint

1. There are quite a few ways of solving this problem, but you will need to use the `range()` function in any of the solutions.

# Solution

[https://repl.it/@appbrewery/day-5-3-solution](https://repl.it/@appbrewery/day-5-3-solution)
'''

#Write your code below this row 👇
# Determine the range logic to get a list of even numbers
# l=[]
# for number in range(2,101,2):
#   l.append(number)
# print(l)

# #  Calculate total for even numbers from 1-100
total = 0
for number in range(2,101,2):
  total += number
print(total)

# Calculate total for even numbers from 1-100 using Modulo
total2 = 0
for number in range(1,101):
  if number%2==0:
    total2 += number
print(total2)
