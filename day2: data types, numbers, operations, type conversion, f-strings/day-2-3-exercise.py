######## Notes from lecture
"""
print(int(8 / 3)) # This returns only the value before decimals
print(round(8 / 3)) # Rounds to a whole number
print(round(8 / 3, 2)) # Indicate precision, here return two decimal places
print(8 // 3) # Floor division - If you want just an integer without cast/coverting to an integer
print(type(8 / 3)) # Returns a float
print(type(8 // 3)) # Returns an int 
result = 4 /2 # Create a variable
result /= 2 # You can continue calculation on the value returned from result by using the notation of /,*,+,- with =
result /= 2
print(result)
score = 0
print ("Your score is " + str(score)) # score is an int, convert to str to print
height = 1.8
isWinning = True
# f-string will allow you to print mixed datatypes instead of having to cast/convert the datatypes to string. The f must go before the quotations, then use {} to include your variables
print(f"Your score is {score}, your height is {height}, and you are winning is {isWinning}.")
"""



######## Exercise - Your Life in Weeks
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.

#Where x, y and z are replaced with the actual calculated numbers.

#Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(type(age))

age_as_int

years_left = 90 - age_as_int
#print(years_left)
#print(type(years_left))

months_left = years_left * 12
#print(months_left)

weeks_left = years_left * 52
#print(weeks_left)

days_left = years_left * 365
#print(days_left)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")