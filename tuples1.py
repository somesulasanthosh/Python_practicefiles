# tuple_1 = ()
# print(tuple_1)
# print(type(tuple_1))


# tuple_2 = (1,2,5.7,"santhosh",True,(1,2,3),25,25,25)
# print(tuple_2)
# print(type(tuple_2))


# tuple_3 = tuple()
# print(tuple_3)
# print(type(tuple_3))


# a=b=c=d = 1
# print(a)
# print(b)
# print(c)
# print(d)


# a = 1,23,4,5.7,True,"pythonlife"
# print(a)

# a,b,c,d = 1,2,3,4
# print(a)
# print(b)
# print(c)
# print(d)


#swapping of two variables without using third variable
# a = 10
# b = 20
# a,b = b,a
# a = a+b
# b = a-b
# a = a-b
# print(a)#20
# print(b)#10

# person_info = ('John', 25, 'Male')
# print(len(person_info))


# tuple_2 = (1,2,3,4,"pythonlife",True,5.7,(1,2,3),[1,2,3],25,25,25,25,25,0,False)
# print(tuple_2.count(1))

# tuple1 = (1, 2, 3)
# tuple2 = ('a', 'b', 'c')
# print(tuple1+tuple2)


# tuple1 = (1, 2, 3)
# print(tuple1*3)


# sample = (1,2,3,4)
# print(sample[2])
# print(sample[-2])


# sample = (1,2,3,4)
# #seq[s:s:s]
# print(sample[1:3])
# print(sample[::-1])



# numbers = (1, 2, 3, 4, 3, 5,"pythonlife")
# index_of_three = numbers.index("pythonlife")
# print(index_of_three)



# fruits = ('apple', 'banana', 'orange')
# is_apple_present = 'apple' in fruits
# print(is_apple_present)


# sample = ()
# print(all(sample))


# Coding Exercise:

# Create a Tuple Write a program that creates a tuple containing three 
# elements: your name, your age, and your favorite color. Then print the tuple.

# my_tuple =("santhosh",22,"sky blue")
# print(my_tuple)

# Access Tuple Elements Write a program that creates a tuple containing the 
# days of the week. Then, print the third element of the tuple.

# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(days[3])

#  Tuple Concatenation Write a program that creates two tuples, one 
# containing odd numbers from 1 to 5 and another containing even numbers 
# from 2 to 6. Concatenate these two tuples and print the result.

# odd_numbers = (1, 3, 5)
# even_numbers = (2, 4, 6)
# all_numbers = odd_numbers + even_numbers
# print(all_numbers)


# Tuple Unpacking Write a program that defines a tuple containing the 
# dimensions of a rectangle (length and width). Then, unpack this tuple into 
# two variables and calculate the area of the rectangle.

# rectangle = (10, 5)   
# length, width = rectangle
# area = length * width
# print("Length:", length)
# print("Width:", width)
# print("Area of Rectangle:",area)


# Check if an Element Exists Write a program that checks if a given element exists in a tuple
# numbers = (10, 20, 30, 40, 50)
# element = 60
# if element in numbers:
#     print("Element exists in the tuple")
# else:
#     print("Element does not exist in the tuple")


# Write a Python program to generate a bill for a supermarket purchase. The 
# program should store the items and their prices in a list of tuples. It should 
# then iterate over this list to print out each item along with its price. Finally, 
# calculate and print the total cost of all the items


items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
total = 0
print("Item\t\tPrice")
print("-------------------")
for item, price in items:
    print(f"{item}\t\t{price:.2f}")
    total += price
print("-------------------")
print(f"Total\t\t{total:.2f}")