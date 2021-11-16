######## Notes from lecture
'''
List: data structure, a way to organize and storing data in Python

We use variable to store one piece of data, for example:
a = 3
b = "hello"
When you need to store grouped pieces of data; data that has some sort of connectionw ith each other. For example, if you wanted to store all names of states in the US, it won't make sense to store them individually, since they sort of belong together, they have a relationship to each other. It would be if you had a variable called states_in_US, and you can store all the names of the states in one variable. Or perhaps you want to maintain order, for example a list of individuals in line. You may want to keep their order so that the last person does not jump the line. Introducing lists...

fruits = [item1, item2]
In python, LISTS always starts and end with square brackets []. In between, you have items separated by commas. Order is determined by the order in the list.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]


To reference an item in the list, you can indicate the index/offset of the item you want in brackets

print(states_of_america[2])

If I use negative index, it will start counting from the end of the list:
print(states_of_america[-1])

So far, we have only fetched data from a list based on indeces. We can also grab a hold of an item from the list and change/alter it:
states_of_america[1] = "Pencilvania"
print(states_of_america)

You can add to the list:
states_of_america.append("Lunaland")
print(states_of_america)

states_of_america.extend(["Kittyland", "Sorinland"])
print(states_of_america)

More things you can do with lists:
https://docs.python.org/3/tutorial/datastructures.html

You can convert a string into a list by using str.split(",")


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
print(dirty_dozen)

How can we separate these out into fruits and vegetables?
You can technically create two lists (fruits and vegatables)
But, in this scenario, we have determined that the fruits and vegetables have a relationship. They're part of the dirty dozen. So, we can create a list within a list, this is called nested list:

fruits = ["Strawberries", "Nectarines", "Apples", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
'''

######## Exercise - Who's Paying?
# Instructions
'''
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

**Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input
Angela, Ben, Jenny, Michael, Chloe

Note: notice that there is a space between the comma and the next name. 


# Example Output
Michael is going to buy the meal today!

'''

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names)

# len() can return the number of items (length) in an object and works with lists, typles, and range. len() can return number of elements in a list or number of characters ina string 
count = len(names)
# print(count)

import random
random_list = random.randint(0,count-1) 
# print(random_list)

random_person = names[random_list]
# print(random_person)
print(f"{random_person} is going to buy the meal today!")




######## Angela's solution
# Get total number of items in list:
num_items = len(names)

random_choice = random.randin(0, num_items - 1)

person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")

##### Using choice():
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")
