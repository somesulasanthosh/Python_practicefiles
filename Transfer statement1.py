# Syntax:
# for item in iterable:
#     if condition:
#         break

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# print(f"last iteration {i}")


# emp_id = [19,150,60,7,5,100,600,9850,9845,9848,91,79,3,28,10,11,23,13]
# for i in emp_id:
#     if i == 600:
#         print(f"employe id found {i}")
#         break

# print(f"last iteration {i}")



# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

# print(f"last iteration {i}")


# products = ["ok","ok","ok","ok","defect","defect","ok","ok","ok","defect"]
# for i in products:
#     if i == "defect":
#        continue
#     print(i)

# print(f"last iteration {i}")



# products = ["ok","ok","ok","ok","defect","defect","ok","ok","ok","defect"]
# for i in products:
#     if i == "defect":
#        print(i)

# print(f"last iteration {i}")


# if cond:
    #block of code to be executed

# num_1 = 10
# if num_1>=5:
#     pass
# else:
#     print(f"not required")


# for i in range(10):
#     pass

# print(f"last iteration {i}")


# **Problem 1: Using `break` in a For Loop**

# Write a Python program that takes a list of numbers as input `numbers = [25, 30, 20, 40, 15, 25]` and prints the sum of the numbers. However, if the sum exceeds 100, stop adding numbers and print "Sum exceeded 100".


# numbers = [25, 30, 20, 40, 15, 25]
# sum = 0
# for i in numbers:
#     sum+=i
#     if sum>100:
#         break
# print(f"sum exceeded 100")
# print(f"sum {sum}")


#  Exercise
# Write a Python program that takes a list of numbers as input 
# numbers = [25, 30, 
# 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds 
# 100, stop adding numbers and print "Sum exceeded 100"

# numbers = [25, 30, 20, 40, 15, 25]

# total = 0

# for num in numbers:
#     total += num
    
#     if total > 100:
#         print("Sum exceeded 100")
#         break

# print("Current Sum:", total)



# Write a Python script that uses a for loop to iterate through numbers from 1 to 
# 600. Print only the odd numbers, skipping the even ones using the 
#  continue statement.

# for num in range(1, 601):

#     if num % 2 == 0:
#         continue
#     print(num)


# Write a Python script that checks if a number is even or odd. If the number is 
# even, print "Even"; if odd, do nothing (use the 
# pass statement)

# number = 8

# if number % 2 == 0:
#     print("Even")
# else:
#     pass



# Write a Python script that iterates through a list of words. If the word is "break," 
# exit the loop using the 
# break statement. If the word is "skip," skip the rest of the 
# code for the current iteration using the 
# continue statement. For any other word, 
# print the word

words = ["hello", "python", "skip", "world", "break", "coding"]

for word in words:
    if word == "skip":
        continue
    if word == "break":
        break
    print(word)