# # def sample(a,b):#function definition
# #     return a+b
# # obj = sample(10,10)
# # print(obj)


# # lambda args:exp
# result = lambda a,b:a+b
# print(result(10,10))

# print((lambda a,b,c,d:a+b+c+d)(10,10,10,10))


# # Syntax:
# # filter(function, iterable)
# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# empty_list = []
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)



# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def even(a):
#     return a%2==0
# obj = even(24)
# print(obj)



# #syntax
# # filter(func,iterable)
# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def even(a):
#     return a%2==0
# result = filter(even,list_1)
# print(list(result))

# #lambda args:exp
# filter(func,iterable)
# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# result = filter(lambda a:a%2==0,list_1)
# print(list(result))


# # Syntax:
# # map(function, iterable, ...)

# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# empty_list = []
# for i in list_1:
#     result = i**2
#     empty_list.append(result)
# print(empty_list)

# def square(a):
#     return a**2
# obj = square(8)
# print(obj)


# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def square(a):
#     return a**2
# result = map(square,list_1)
# print(list(result))

# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# list_2 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# result = map(lambda a,b:a**b,list_1,list_2)
# print(list(result))


# from functools import reduce
# reduce(func,iter,initialize-->optional)


# def add(a,b,c,d):
#     return a+b+c+d
# obj = add(10,10,10,10)
# print(obj)


# from functools import reduce
# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# def add(a,b):
#     return a+b
# result = reduce(add,list_1)
# print(result)


# from functools import reduce
# list_1 = [23,4,5,67,2,35,84,1,2,3,4,5,6,7,8,9,10,45,18,24,89,50,4]
# result = reduce(lambda a,b:a+b,list_1)
# print(result)
# sum = 0
# total = 0









# def sample():
#     yield 1#pause or hold
#     yield 2#pause or hold
#     yield "pythonlife"#pause or hold
# obj = sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())





# Coding exercises:

# Write a Python function 
# square_all(numbers) that takes a list of numbers as input 
# and returns a new list containing the square of each number in the input list. 
# Use the 
# map() function with a lambda function to implement this.

# def square_all(numbers):
#     return list(map(lambda x:x**2,numbers))
# numbers = [1,2,3,4,5,6]
# result =square_all(numbers)
# print(result)


# Write a Python function 
# filter_positive(numbers) that takes a list of numbers as 
# input and returns a new list containing only the positive numbers from the 
# input list. Use the 
# filter() function with a lambda function to implement this.


# def filter_positive(numbers):
#     return list(filter(lambda x: x > 0, numbers))
# numbers = [-10, 5, -3, 8, 0, 12, -1]
# result = filter_positive(numbers)
# print(result)


# Write a Python function 
# calculate_factorial(n) that calculates the factorial of a 
# given number n. Use the 
# reduce() function with an appropriate lambda 
# function to implement this


from functools import reduce
def calculate_factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
number = 5
result = calculate_factorial(number)
print(result)


# Write a Python function 
# count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. Use the 
# reduce() 
# function with an appropriate lambda function to implement this.



from functools import reduce
def count_vowels(string):
    vowels = "aeiouAEIOU"
    
    return reduce(
        lambda count, char: count + (1 if char in vowels else 0),
        string,
        0
    )
text = "Hello World"
result = count_vowels(text)
print(result)