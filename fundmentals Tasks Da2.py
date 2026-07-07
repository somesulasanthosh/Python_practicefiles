# Create a Python script with both single-line and multi-line comments 
#explaining the purpose of the script
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)
count = len(numbers)
average = total_sum / count
print("Numbers:", numbers)
print("Sum:", total_sum)
print("Count:", count)
print("Average:", average)

# output
#Numbers: [10, 20, 30, 40, 50]
#Sum: 150
#Count: 5
#Average: 30.0

#Declare two variables, one storing an integer and the other a string. Print their values

age = 22
name ="santhosh"
print(age)
print(name)

# output
#22
#santhosh

#Write a program that prints a pattern using multiple print statements
print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")
print("* * * * * *")
print("* * * * * * *")
print("* * * * * * * *")
print("* * * * * * * * *")
print("* * * * * * * * * *")

# output
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * * * *
#* * * * * * *
#* * * * * * * *
#* * * * * * * * *
#* * * * * * * * * *

#Create a Python script for a simple task and add comments to explain each step

# Step 1: Take input from the user
number = int(input("Enter a number: "))

# Step 2: Check if the number is divisible by 2
if number % 2 == 0:
    # Step 3: If divisible by 2, it is even
    print("The number is Even")
else:
    # Step 4: If not divisible by 2, it is odd
    print("The number is Odd")

# Step 5: End of program
print("Program completed.")

#output
#Enter a number: 2
#The number is Even
#Program completed.

#Create variables of different data types(int,float,str) and print their values
age = 22
salary = 50000.75
name ="Santhosh"
print("Integer value (age):", age)
print("Float value (salary):", salary)
print("String value (name):", name)

#output
#Integer value (age): 22
##Float value (salary): 50000.75
#String value (name): Santhosh

#Determine the data type of a variable.
# Expected Output:
# The data type of variable discount is <class 'int'>

discount = 10
print(type(discount))

#output
#<class 'int'>

# Display the memory addresses
# The memory addresses of x and y 

employee_id = 10
person_age = 22
print(id(employee_id))
print(id(person_age))

# output
#140723308889496
#140723308889496

#Create a program that takes user age = “35ˮ, converts it to an integer, and then prints the result type

age = "22"
age = int(age)
print(age)
print(type(age))

# output
#22
#<class 'int'>

#Concatenate two strings and print the result

first_name = "Somesula"
last_name = "Santhosh"
full_name = first_name + " " + last_name
print(full_name)
