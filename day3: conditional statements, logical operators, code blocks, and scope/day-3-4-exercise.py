# ######## Notes from lecture
# # Rollercoaster Tickets
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age<= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")

#   photo = input("Do you want a photo taken? Y or N.")
#   if photo == 'Y':
#     #Add $3 to their bill
#     bill = bill + 3 #or bill +=3

#   print(f"You final bill is ${bill}")
# else:
#   print("You do not meet the height requirement to ride the rollercoaster.")

######## Exercise Pizza Order
# Instructions

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

# Based on a user's order, work out their final bill. 
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill += 2

if size == 'M':
  bill = 20
  if add_pepperoni == 'Y':
    bill += 3

if size == 'L':
  bill = 25
  if add_pepperoni == 'Y':
    bill += 3

if extra_cheese == 'Y':
  bill += 1
print(f"Your final bill is: ${bill}.")


### Angela's solution
bill = 0

if size == 'S':
   bill += 15
elif size == 'M':
  bill += 20
else size == 'L':
  bill += 25

if add_pepperoni == 'Y':
  if size == 'S':
    bill += 2
  else:
    bill += 3

if add_cheese -- 'Y':
  bill += 1

print(f"You final bill is: ${bill}.")


