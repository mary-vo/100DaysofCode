######## Notes from lecture
#  Built in functions for Python
print("Hello")
num_char = len("Hello")
print(num_char)

#  To create our own function
def my_function(): #def followed by a name for the function and (), everything related to the function should be indented
  print("Hello")
  print("Bye")
#  At this point, if we run the code, nothing happens. Becuase we have not executed the function. To trigger the function or "call the function", refer to the name of the function and include any input required in the function
my_function()


###### Exercise - Reeborg's World
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19115132#questions

def turn_right():
    for i in range(3):
        turn_left()

## Below is two ways to do this, I think the second method is better      
# Define a for loop that goes through repeated steps
def complete_hurdle():
    for i in range(6):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

complete_hurdle()

# Define a variable, then use a for loop to iterate through the variable 6 times 
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()   
    
for step in range(6):
    jump()

# Ways to solve for at_goal situation
while not at_goal():
  jump()

while at_goal() == False:
  jump()

while at_goal() != True:
  jump()


## HURDLE 3
  def turn_right():
    for i in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()   
    
while not at_goal():
    if wall_in_front() != True:
        move()
    elif front_is_clear() != True:
        jump()


## HURDLE 4
def turn_right():
    for i in range(3):
        turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

  
###  While loop
# This loop continues while a particular condition is true
# For loops so far:

#  Looping through item in list
for item in list_of_items:
  #Do something to each item

# With a range function, where we create a range between a,b and then we use every number in that range to do something
for number in range(a,b):
  print(number)

#  While loop
while something_is_true: #while followed by a condition we want to test
  #Do something repeatedly
# Example of while loop using hurdles exercise
number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -= 1
  print(number_of_hurdles)

###  When to use "for loop" vs. "while loop:
# for loop is great to iterate over something and you need to do something with each thing that you're iterating over, example:
# iterate over list, and you want to do something each element in the list

fruits = ["Apple", "Pear", "Orange"]
for fruit in fruits:
  print(fruit)

for n in range(1,6):
  print(n)
  
# while loop when you don't care what number in sequence you're in which item you're iterating through, you just want to carry out a functionality many many times until a condition is met. While loops can be more dangerous--they will continue running until the condition is finally met or becomes "false". If it never becomes false, then you end up with an infinite loop. For loops have an upper limit (for example iterating over a list or range)

# Infinite loop
while 5 > 3: #5 will ALWAYS be greater than 3, you're stuck in an infinite loop. TO DEBUG through an infinite loop, within the while loop, print out the condition
  print(5 >3) #This will keep printing true
  #Do this
  #Then do this