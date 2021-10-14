#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?")
tip = input(f"What percentage tip would you like to give? 10, 12, or 15?")
total_people = input("How many people to split the bill?")
'''
print(type(total_bill))
print(type(tip))
print(type(total_people))
'''

# Calculate total per person

total_bill_as_float = float(total_bill)
tip_as_float = float(tip)
total_people_as_int = int(total_people)

''''
print(type(total_bill_as_float))
print(type(tip_as_float))
print(type(total_people_as_int))
'''
individual_total =  round((total_bill_as_float * (1 + 1/tip_as_float)) / total_people_as_int,2)
#print(individual_total)


print(f"Each person should pay: ${individual_total}")