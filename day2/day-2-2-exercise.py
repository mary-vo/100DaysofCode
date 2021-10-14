######## Notes from lecture
3 + 5
7-4
3*2
# When dividng, result is always a float
print(6/3)
# Exponents
print(2 ** 2)

print(3/3*3/3*3)



######## Exercise - BMI Calculator
# Instructions

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

#The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Determine the type for height and weight (above)
print(type(height))
print(type(weight))

# Cast height and weight to float
height_float = float(height)
weight_float = float(weight)

print(type(height_float))
print(type(weight_float))

# Calculate BMI and cast float to int to get a whole number as a result; print your result
BMI = int(weight_float / (height_float ** 2))
#bmi_as_int = int(BMI)
print(BMI)
#print(bmi_as_int)
