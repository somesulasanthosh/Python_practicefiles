#syntax
# def functionname():#function definition
    # function body

# def sample():#function definition
#     user_name = input("enter the username:")
#     print(f"welcome {user_name}")
# sample()#function calling

# def santhosh():# function body
#     num_1 = 10
#     num_2 = 20
#     print(num_1+num_2)
# santhosh()#function calling

# def add():
#     num_1 = int(input("Enter the number1: "))
#     num_2 = int(input("Enter the number2: "))
#     return num_1+num_2

# obj = add()
# print(obj)

# def mul(num_1,num_2):#function definition
#     return num_1*num_2
# obj = mul(10,10)#here, 10,10 are the arguments passed to the function parameters
# print(obj)


# arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)

# def sample(*a):
#     return a
# obj = sample("pythonlife",1,2,3,True)
# print(obj)

#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing
# def sample(**a):
#     return a
# obj = sample(a=10,b=20,c=30)
# print(obj)

#*--> tuple
#**--> dict

# def details(user=None,empid=None,dept=None):#function definition
#     print(user,empid,dept)
# details("kiran",1234,"python developer")
# details("vasu",4567,)
# details("raju",)
# details("santhosh",1234,"power bi developer")
# details()

# def discount_1(price,discount=20):
#     discount = (price*discount)/100
#     final_price = price - discount
#     return final_price
# print(discount_1(10000))
# print(discount_1(20000))
# print(discount_1(30000))
# print(discount_1(50000))
# print(discount_1(100000,50))




# variables --> two types 
# 1. local variables --> function(within the function)
# 2. global variable --> outside the function


# def details():
#     user = "kiran"
#     emp_id = 1234
#     salary = 200000
#     print(user)
#     print(emp_id)
#     print(salary)
#     hike = 50000
#     salary += hike
#     print(f"salary after hike {salary}")
# details()



# balance = 1000
# def credit(amount):
#     global balance
#     print(f"amount credited {amount}")
#     balance += amount
#     print(f"account balance {balance}")

# credit(10000)



# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(float(a**b))
# def div(a,b):
#     print(a/b)


add(10,10)
add(20,40)
expo(4,4)
