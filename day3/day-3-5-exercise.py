## Love Calculator
# 💪 This is a Difficult Challenge 💪
# Instructions
'''
You are going to write a program that tests the compatibility between two people.  

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 


For Love Scores **less than 10** or **greater than 90**, the message should be:

`"Your score is **x**, you go together like coke and mentos."` 

For Love Scores **between 40** and **50**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`
'''



# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

combined_name = name1+name2
combined_name_upper = combined_name.upper()
# print(combined_name)

count_T = combined_name_upper.count('T')
count_R = combined_name_upper.count('R')
count_U = combined_name_upper.count('U')
count_E = combined_name_upper.count('E')
count_L = combined_name_upper.count('L')
count_O = combined_name_upper.count('O')
count_V = combined_name_upper.count('V')
count_E = combined_name_upper.count('E')

# print(count_T)
# print(count_R)
# print(count_U)
# print(count_E)

# print(count_L)
# print(count_O)
# print(count_V)
# print(count_E)

sum_true = str(count_T + count_R + count_U + count_E)
sum_love = str(count_L + count_O + count_V + count_E)
# print(sum_true)
# print(sum_love)
# print(type(sum_true))
 
love_score = int(sum_true + sum_love)
# print(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")