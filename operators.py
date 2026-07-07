## practice##

#operator ---> symbol or keyword that performs an operation on one or more operands
#operand --->  Value or variable acted  upon by an operator to produce a result


#  (+)
# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)


# (-)
# num_1 = 10
# num_2 = 25
# result = num_2 - num_1
# print(result)



# * (Multiplication): Multiplies two operands.
# num_1 = 10
# num_2 = 5
# result = num_1 * num_2
# print(result)


# ** (Exponentiation): Raises the base (left operand) to the power of the exponent (right operand).

# num_1 = 10
# num_2 = 5
# result = num_2 ** num_1
# print(result)
# print(f"base value is {num_2} and expo value is {num_1} final result {num_2**num_1}")




# / (Division): Divides the left operand by the right operand.
# num_1 = 10
# num_2 = 3
# result = num_1 / num_2
# print(result)


# num_1 = 10
# num_2 = 3
# result = num_1 // num_2
# print(result)


# % (Modulus): Returns the remainder of the division of the left operand by the right operand.
# num_1 = 10
# num_2 = 3
# result = num_1 % num_2
# print(result)



# a = 10
# b = 3

# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponentiation = a ** b

# print(addition, subtraction, multiplication, division, remainder, floor_division, exponentiation)






# num_1 = 10
# num_1 += 5 #eq-->num_1 = num_1 + 5
# print(num_1)


# num_1 = 10
# num_1 *= 5 #eq-->num_1 = num_1 * 5
# print(num_1)

# TASK

#-=
# num_1 =20
# num_1 -= 5 #eq-->num_1 = num_1 - 5
# print(num_1)

#/=

# num_1 = 30
# num_1 /= 5
# print(num_1)


#//=

# num_1 = 40
# num_1 //= 5
# print(num_1)



# product_cost = 1000
# product_cost_2 = 1000
# print(product_cost == product_cost_2)
# print(product_cost != product_cost_2)
# print(product_cost < product_cost_2)
# print(product_cost <= product_cost_2)
# print(product_cost > product_cost_2)
# print(product_cost >= product_cost_2)


# user_name = "varun"
# pass_word = "aravind@123"
# print(user_name == "varun" and pass_word == "aravind@123") 



# user_name = input("enter the username: ")
# pass_word = input("enter the password: ")
# print(user_name == "ashish" or pass_word == "1234") 


# sample = True
# print(not sample)

# sample = False
# print(not sample)


# a = [1,2,3,4,"pythonlife"]
# print(id(a))
# b = [1,2,3,4,"pythonlife"]
# print(id(b))
# print(a is b)
# print(a is not b)


# a = 1000**1000
# print(id(a))
# b = 1000**1000
# print(id(b))
# print(a is b)


# products_data = ["iphone16","samsungs25","oppo reno","vivox300"]
# print("redmi note 15" in products_data)
# print("iphone16" in products_data)
# print("micromax" not in products_data)


# sentence = "pythonlife"
# print("python" in sentence)



# product_cost = 100000
# discount = 10
# result = product_cost * (discount/100)
# product_cost -= result #eq-->pc = pc - r
# print(product_cost)
# print(f"discount given {discount}% and final discount {result} and total cost after discount Rs{product_cost}/-")


# a = 10
# b = 2
# result = (a+b)**2
# print(result)


# Coding Exercise Task 1

# Create a program that takes user input for their name and age. 
# Use formatted strings (f-strings) to print a message welcoming the user and
# stating their age

# name = input("enter your name: ")
# age  = input("enter your age: ")
# print(f"welcome {name}! your age {age} yours old")

#  Create a list called 
# numbers that contains integers from 1 to 10

# Check if the number 5 is in the list
# Check if the number 15 is not in the list

# numbers = list(range(1, 11))
# print("Is 5 in the list?", 5 in numbers)
# print("Is 15 not in the list?", 15 not in numbers)


# Coding Exercise  Task 2

# Write a Python program to calculate the area of a rectangle using the given 
# formula: 
# area = length * width . Take the values of length and width as inputs from 
# the user

# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width
# print(f"The area of the rectangle is: {area}")


# Write a Python program to demonstrate incrementing and decrementing a variable

# num = 20
# print("Initial value:", num)
# num = num + 1
# print("After increment:", num)
# num = num - 1
# print("After decrement:", num)


# Write a Python program to convert temperature from Celsius to Fahrenheit. The 
# formula for conversion is: 
# F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user


# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Temperature in Fahrenheit is: {fahrenheit}")



# Write a Python program to calculate the simple interest given the principal 
# amount, rate, and time (in years)

# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest (per year): "))
# time = float(input("Enter the time (in years): "))
# simple_interest = (principal * rate * time) / 100
# print(f"The Simple Interest is: {simple_interest}")

# Write a Python program to concatenate two strings and display the result. The 
# strings should be taken as input from the user

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# result = str1 +" "  + str2
# print(f"Concatenated string: {result} ")


# Write a Python program to convert a distance from kilometers to miles

kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(f"Distance in miles: {miles}")