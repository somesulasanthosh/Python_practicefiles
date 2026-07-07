# #types of errors
# 1.syntax errors
# 2.runtime errors
# 3.logical errors -->(--> user need to indentified (very difficult to find))


# num_1 = 10
# num_2 = 5
# result = num_1 - num_2
# print(result)


#syntax --> compiled time errors
# print(exp)
# print(10+10)


# if cond:
    #block of code


# age = 35
# if age>=18:
#     print(f"elgible to vote")


# for item in seq:
    #block of code

# for i in range(10):
#     print(i)


# runtime errors --> which disturbs the flow of execution (during the execution) also called exception

# num_1 = int(input("Enter the num_1: "))
# num_2 = int(input("Enter the num_2: "))
# print(num_1 + num_2)
# print(num_1 - num_2)
# print(num_1 * num_2)
# try:
#     print(num_1 / num_2)
# except:
#     print("error occured")
# print(num_1 + num_2)
# print(num_1 - num_2)



# list_1 = [10,20,30,40,50]
# print(list_1[2])
# print(list_1[3])
# try:
#     print(list_1[0])
#     print(list_1[1])
# except:
#     print(f"error occured")
# print(list_1[0])



num_1 = int(input("enter the number1: "))
num_2 = int(input("enter the number2: "))
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
try:
    print(num_1 / num_2)
except:
    print(f"error occured")
else:
    print(num_1 ** num_2)
finally:
    print(f"no code to execute.")






# try:
#     num_1 = int(input("enter the number1: "))
#     num_2 = int(input("enter the number2: "))
# except ValueError as e:
#     print(e)
# else:
#     print(num_1+num_2)


# num_1 = int(input("enter the number1: "))
# num_2 = int(input("enter the number2: "))
# try:
#     print(num_1/num_2)
# except ZeroDivisionError as e:
#     print(e)




# list_1 = [10,20,30,40,50]
# print(list_1[2])
# print(list_1[3])
# try:
#     print(list_1[8])
#     print(list_1[1])
# except IndexError as e:
#     print(e)



# try:
#     num_1 = int(input("enter the number1: "))
#     num_2 = int(input("enter the number2: "))
#     print(num_1/num_2)
#     list_1 = [10,20,30,40,50]
#     print(list_1[8])
# except Exception as e:
#     print(e)
