# (+)
# a = 10
# b = 20
# print(a+b)

# a = "kiran"
# b = "raju"
# print(a+b)



# class calculator():
#     def add(self,a,b,c):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj = calculator()
# obj.add(10,10,10)



# class calculator():
#     def add(self,a=40,b=20,c=10):
#         print(a+b+c)

# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10)
# obj.add(10)
# obj.add()



# class calculator():
#     def add(self,a=40,b=None,c=None):
#         print(a,b,c)

# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10,"kiran")
# obj.add(10,"ravi")
# obj.add(5.7,10)


#2.method overriding
# method overriding --> method name should be same arguments should be also same 

# class father():
#     def details(self,a,):
#         print(f"this is father class. {a}")

# class child(father):
#     def details(self, a):
#         print(f"this is derived class {a}")
#         super().details("100cr")
# obj = child()
# obj.details("100cr")

# Public  
# protect _
# private __


# class gfather():
#     def __init__(self,a):
#         self.a = a
#         print(f"this is base class gfather {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is derived class father {self.a}")
# obj = father("100cr")
# obj.details()



# Public  
# protect _
# private __

# class gfather():
#     def __init__(self,a):
#         self._a = a
#         print(f"this is base class gfather {a}")
# class father(gfather):
#     def details(self):
#         print(f"this is derived class father {self._a}")
# obj = father("100cr")
# obj.details()




# Public  
# protect _
# private __
class gfather():
    def __init__(self,a):
        self.__a = a
        print(f"this is base class gfather {a}")
class father(gfather):
    def details(self):
        print(f"this is derived class father {self.__a}")
obj = father("100cr")
obj.details()

