# for variable in sequence:
    # code to be executed



# emp_data = ["santhosh","sree ram","suresh","harish","charan","bunny"]
# for i in emp_data:
#     print(f"welcome to pythonlife")
#     print(f"welcome {i}")



# fruits = ("guva","watermelon","grapes","pomegranate","carrot","cukumber")
# for i in fruits:
#     if i == "watermelon":
#         print(f"{i} has been received")



# with else statement

# fruits = ("guva", "watermelon", "grapes", "pomegranate", "carrot", "cukumber")

# for i in fruits:
#     if i == "watermelon":
#         print(f"{i} has been received")
#     else:
#         print(f"{i} has not received")


# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# for i in range(10):
#     print(i)


# for i in range(10):
#     user = input("Enter the username: ")
#     print(user)


# for i in range(1,100):
#     print(i)


# for i in range(1,11,5):
#     print(i)



#multiplication of Tables
# for i in range(1,11):
#     print(f"2 X {i} = {2*i}")


# for i in range(1,11):
#     print(f"12X {i} = {12*i}")

# table = int(input("enter the table: "))
# for i in range(1,11):
#     print(f"{table} X {i} = {table*i}")


# for i in range(3):
#     print(i)


# for i in seq:#outer for loop
#     for j in seq:#inner for loop


# for i in range(3):#outer for loop
#     for j in range(3):#inner for loop
#         print(i,j)


# for i in range(1,11):
#     for j in range(1,11):
#        print(f"{i} X {j} = {i*j}")
#     print("-"*25)


# while cond:
    #block of code executed


# age = 35
# while age>=18:
#     print(f"elgible to vote")


# while True:
#     user_name = input("enter the username: ")
#     password = input("enter the password: ")
#     if user_name == "santhosh" and password == "santhosh@123":
#         print(f"login success..")
#         print(f"welcome {user_name}")
#         break
#     else:
#         print(f"invalid credentials..")


# count = 0
# while count<3:
#     print(count)
#     count +=1



# while cond:
#     while cond:


# while True:#outer while loop
#     print("welcome to pythonlife")
#     print("hello everyone")
#     while True:#inner while loop
#         print("join session by 7 pm")
#         print(f"zoom invitation has been sent")
#         break
#     break


# Exercise 1: Sum of Squares
# Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop.


sum=0
# for n in range(1,6):
#     sq=n**2
#     sum+=sq
# print(f"sum of squares of numbers:{sum}")



# Write a Python program that uses a while loop to print a countdown from 5 to 1.

# count = 5
# while count>0:
#     print(count)
#     count -=1


# Write a Python program to print the multiplication table for a user-specified number using a nested for loop.

# table = int(input("Enter the table: "))
# for i in range(1,11):
#     for j in range(1,2):
#         print(f"{table} X {i} = {table*i}")


# table = int(input("Enter the table: "))
# for i in range(1,2):
#     for j in range(1,11):
#         print(f"{table} X {j} = {table*j}")


# Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive).

# sum_even = 0

# for i in range(0, 11):
#     if i % 2 == 0:
#         sum_even += i

# print("Sum of even numbers:", sum_even)


#  Calculate the sum of all numbers from 1 to a given number

# number = int(input("enter the number: "))
# sum = 0
# for i in range(1,number+1):
#     sum += i

# print(f"sum of given numbers {number} is {sum}")


# Display numbers from a list using loop

# numbers = [10, 20, 30, 40, 50]

# for i in numbers:
#     print(i)


# Display numbers from 10 to 1 using for loop

# for i  in range(-10,-1+1):
#     print(i,end=" ")


# Write a Python program to print the cube of all numbers from 1 to a given 
# number

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print(f"Cube of {i} is {i**3}")


