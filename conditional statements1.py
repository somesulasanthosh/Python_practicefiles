# Syntax:
# if condition:
#      statement 1
#      statement 2
#      statement n

# age = 35
# if age>=18:
#     print(f"you are eligible to vote age is {age}")
#     user = input("enter the username: ")
#     print(user)


# age = int(input("enter the age : "))
# if age>=18:
#     print(f"you are eligible to vote age is {age}")
#     user = input("enter the username: ")
#     print(user)


# Syntax:
# if condition:
#     # code block to execute if condition is true
# else:
#     # code block to execute if condition is false

# user_name = input("enter the username: ")
# password = input("enter the password: ")
# if user_name == "santhosh" and password == "santhosh@123":#True
#     print(f"login success..")
#     print(f"welcome {user_name}")
# else:
#     print(f"invalid credentials..")


#     user_name = input("enter the username: ")
# password = input("enter the password: ")
# if user_name == "sriram" and password == "santhosh@123":#flase
#     print(f"login success..")
#     print(f"welcome {user_name}")
# else:
#     print(f"invalid credentials..")






# marks = int(input("enter the marks: "))
# if marks>=90 and marks<=100:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80 and marks<=90:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70 and marks<=80:
#     print(f"you got C grade obtained marks {marks}")
# elif marks>=60:
#     print(f"you got D grade obtained marks {marks}")
# elif marks>=35:
#     print(f"passed obtained marks {marks}")
# elif marks<=34 and marks>=0:
#     print(f"you got failed")
# else:
#     print(f"please enter marks in between 0 to 100")




#GRADING system
# marks = int(input("enter the marks: "))
# if marks>100 or marks<0:
#     print(f"please enter marks in between 0 to 100")
# elif marks>=90:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70:
#     print(f"you got C grade obtained marks {marks}")
# elif marks>=60:
#     print(f"you got D grade obtained marks {marks}")
# elif marks>=35:
#     print(f"passed obtained marks {marks}")
# else:
#     print(f"you got failed")




# Syntax:
# if condition1:
#     # code block for condition1
#     if condition2:
#         # code block for condition2
#     else:
#         # code block for condition2 being false
# else:
#     # code block for condition1 being false



# user_name = input("enter the username: ")
# password = input("enter the password: ")
# if user_name == "srinu":#outer if condition
#     if password == "srinu@1234":#inner if condition
#         print(f"login success")
#         print(f"welcome {user_name}")
#     else:
#         print(f"invalid password.")
# else:
#     print(f"invalid username")


# Syntax:
# result = value_if_true if condition else value_if_false


# num_1 = int(input("enter the number: "))
# if num_1%2==0:
#     print(f"{num_1} is even number")
# else:
#     print(f"not even")


# result = value_if_true if condition else value_if_false
# num_1 = int(input("enter the number: "))
# result = "even number" if num_1%2==0 else "not even"
# print(result)


# num_1 = int(input("enter the number: "))
# print(f"{num_1} is even") if num_1%2==0 else print(f"not even")





#Exercsise

# Vowel Checker:
# Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement.

# char = input("Enter the character: ")
# if char=="a" or char =="e" or char == "i" or char  == "o" or char == "u":
#     print("vowel")
# else:
#     print("not vowel")


# char = input("Enter the character: ")
# vowels = ["a","e","i,"u"]
# if char in vowels:
#     print(f"vowel")
# else:
#     print(f"not vowel")



# char = input("Enter the character: ")
# vowels = "aeiouAEIOU"
# if char in vowels:
#     print(f"vowel")
# else:
#     print(f"not vowel")


# char = input("Enter the character: ")
# vowels = ("a","e","i","u") # Tuple
# if char in vowels:
#     print(f"vowel")
# else:
#     print(f"not vowel")


# Age Group Classification
# Write a program that takes an age as input and classifies the person into 
# one of the following age groups:
# Child: 012 years
# Teenager: 1317 years
# Adult: 1864 years
# Senior: 65 years and older

# age = int(input("Enter your age: "))

# if age >= 0 and age <= 12:
#     print("Child")

# elif age >= 13 and age <= 17:
#     print("Teenager")

# elif age >= 18 and age <= 64:
#     print("Adult")

# elif age >= 65:
#     print("Senior")

# else:
#     print("Please enter a valid age")


#Number Classifier:
# Write a program that takes an integer as input and classifies it as positive, 
# negative, or zero. Use the 
# if-elif-else statement.

# number = int(input("Enter an integer: "))

# if number > 0:
#     print("Positive number")

# elif number < 0:
#     print("Negative number")

# else:
#     print("Zero")


#  Leap Year Checker
# Create a program that checks whether a given year is a leap year or not. A 
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")

# else:
#     print(f"{year} is not a leap year")


# Calculator
# Build a simple calculator program that takes two numbers and an operator 
# (+, -, *, /) as input and performs the corresponding operation

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#     print(f"Result = {num1 + num2}")

# elif operator == "-":
#     print(f"Result = {num1 - num2}")

# elif operator == "*":
#     print(f"Result = {num1 * num2}")

# elif operator == "/":
#     if num2 != 0:
#         print(f"Result = {num1 / num2}")
#     else:
#         print("Division by zero is not allowed")

# else:
#     print("Invalid operator")


#  Short Hand If

# Rewrite the following code using the short-hand if statement

# num_1 = int(input("enter the number: "))
# if % 2 == 0: result = "Even"
# else: result = "Odd"



# Discount Calculator
# Create a program that calculates the final price after applying a discount. 
# The program should take the original price and the discount percentage as 
# input

# original_price = float(input("Enter original price: "))
# discount_percentage = float(input("Enter discount percentage: "))

# discount_amount = (original_price * discount_percentage) / 100
# final_price = original_price - discount_amount

# print(f"Discount Amount = {discount_amount}")
# print(f"Final Price = {final_price}")


#  BMI Calculator
# Write a program that calculates the Body Mass Index BMI using the 
# formula: BMI  weight (kg) / (height (m))^2. The program should take 
# weight and height as input


# weight = int(input("Enter weight in kg: "))
# height = int(input("Enter height in meters: "))

# bmi = weight / (height ** 2)

# print(f"Your BMI is {bmi}")