
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 7-9. Your program should work for different inputs. e.g. any two-digit number.

####################################
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = int(two_digit_number[0])
#print(first_digit)

second_digit = int(two_digit_number[1])
#print(second_digit)

# return type for various variables
#print(type(two_digit_number))
#print(type(first_digit))
#print(type(second_digit))

print(first_digit + second_digit)