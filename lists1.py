# list_1= []
# print(list_1)
# print(type(list_1))


# list_2 = [35,5.7,"pyhtonlife",(1,2,3),True,{1,2},{1:"user1"},24,24,24,24]
# print(list_2)
# print(type(list_2))


# list_3 = list()
# print(list_3)
# print(type(list_3))






my_list = [10, 20, 30, 40, 50]
#syntax
# var[indexvalue]










# my_list = [10, 20, 30, 40, 50]
# print(my_list[1])#20
# print(my_list[-4])#20
# print(my_list[4])#50
# print(my_list[-1])#50
# print(my_list[0])#10
# print(my_list[-5])#10



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# # seq[s:s:s]
# print(my_list[0:8:1])
# print(my_list[0:8])
# print(my_list[0:8])
# print(my_list[::])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[::])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[5:8])#60 70 80
# print(my_list[5:])#60 70 80



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[1:4])
# print(my_list[-7:-4])
# print(my_list[3:5])
# print(my_list[-5:-3])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[2:7])
# print(my_list[-6:-1])








# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[::-1])
# print(my_list[6:3:-1])
# print(my_list[-2:-5:-1])
# print(my_list[2::-1])
# print(my_list[-6::-1])


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][2])
# print(matrix[1][2])
# print(matrix[2][0])
# print(matrix[2][2])



# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[-6::-1])


# for i in range(1,10):
#     print(float(i))




###### May11th#############


#syntax
# .methodname(args)

# numbers  = [1,2,3,4,5,6,7,8,9,10,5,5]
# numbers.append(30)
# print(numbers)

# numbers  = [1,2,3,4,5,6,7,8,9,10,5,5]
# numbers.append([5.6,35,35])
# print(numbers)

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.extend(["pythonlife,santhosh,sree ram",1,2])
# print(numbers)

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# sample = numbers.copy()
# print(f"sample data copy{sample}")
# sample.append("pythonlife")
# print(f"sample data copy{sample}")
# print(f"original data {numbers}")

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.clear()
# print(numbers)


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# print(numbers.count(5))

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# print(numbers.count(13))

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# print(numbers.count(25))


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# print(numbers.index(3))


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# print(numbers.index(9))

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.remove(3)
# print(numbers)

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.remove(5)
# print(numbers)



# list_1 = [15,35,45,25]
# list_1.remove(45)
# print(list_1)


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# object= numbers.pop(0)
# print(numbers)
# print(object*25)

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.insert(0,"pythonlife")
# print(numbers)


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.reverse()
# print(numbers)


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.sort()
# print(numbers)



# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# numbers.sort(reverse= True)
# print(numbers)

# Syntax
# [expression for item in iterable]

# for i in range(11):
#     result = i**2
#     print(result)


# empty_list = []
# for i in range(11):
#         result=i**2
#         empty_list.append(result)
# print(empty_list)

# result = [i**2 for i in range(11)]
# print(result)

# print([i**2 for i in range(11)])



# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# empty_list = []
# for i in numbers:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5]
# result = [i for i in numbers if i%2==0]
# print(result)


# print([i for i in numbers if i%2==0])


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5,5,4,4,4,20,20]
# for i in numbers:
#     if i==4:
#         numbers.remove(5)
    
# print(numbers)


# numbers  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,5,5,5]
# empty_list = []
# for i in numbers:
#     if i!=5:
#         empty_list.append(i)
# print(empty_list)



# list_1 = [4,3, 1, 4, 1, 5, 9,4,24,4,2,4, 2, 6, 5,4,4,4,25,25,4,4,4,4,4,4,4,4,44,25,4,4,4,25,44,25,25,4,3, 1, 4, 1, 5, 9,4,24,4,2,4, 2, 6, 5,4,4,4,25,25,4]
# print(len(list_1))

# exercsise

# Write Python code to reverse the order of elements in the given list 
# Print the reversed list.
# my_list = [10, 20, 30, 40, 50, 11]
# my_list.reverse()
# print(my_list)


# Given two lists list1 and list2 , find and print the common elements between them


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common_elements = []

# for item in list1:
#     if item in list2:
#         common_elements.append(item)

# print(common_elements)


# Create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list

# original_list = [1, 2, 2, 3, 4, 4, 5]

# unique_list = []

# for item in original_list:
#     if item not in unique_list:
#         unique_list.append(item)

# print(unique_list)


# Remove duplicate elements from the given list without duplicates while preserving the order.duplicated_list and print the list

# duplicated_list = [1, 2, 2, 3, 4, 4, 5]

# without_duplicates = []

# for item in duplicated_list:
#     if item not in without_duplicates:
#         without_duplicates.append(item)

# print(without_duplicates)


# Write a Python script that concatenates two lists and prints the result

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# concatenated_list = list1 + list2

# print(concatenated_list)


# Write a Python script that repeats a list three times and prints the result
# my_list = [1, 2, 3]

# repeated_list = my_list * 3

# print(repeated_list)

# Write a Python script that removes the elements at even indices from a list

# my_list = [10, 20, 30, 40, 50, 60]

# result = []

# for i in range(len(my_list)):
#     if i % 2 != 0:
#         result.append(my_list[i])

# print(result)


# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of 
# a list

# my_list = [1, 2, 3, 4, 5]

# my_list = [10, 11, 12] + my_list

# print(my_list)


# List comprehensions
# Words Lengths Given a list of words, create a list containing the lengths of 
# each word

# words = ["apple", "banana", "cherry", "date"]

# word_lengths = []

# for word in words:
#     word_lengths.append(len(word))

# print(word_lengths)




name = "santhosh sree ram"

result = name.title()

print(result)