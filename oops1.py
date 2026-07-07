#syntax
# class cn(): #class definition
#     Attribute #class body
#     methods #class body


# class person_details(): #class definition
#     user_name = "kiran" #attributes
#     emp_id = 1234 #attributes
#     def details(self,a):
#         print(f"he works at ABC company {self.user_name} {a}")
#     def details2(self,):
#         print(f"he own ABC company")
#         self.details()
# #syntax
# # objname = classname()
# kiran = person_details()
# kiran.details("100cr")
# kiran.details2()
# print(kiran.user_name)
# print(kiran.emp_id)




# class feature_phone():
#     brand = "samsung"
#     color = "white"
#     battery = "3000mah"
#     def calling(self,brand_name):
#         print(f"you are calling from {brand_name}... ")
#     def message(self,mn):
#         print(f"message has been sent succesffully to... {mn}")
# ##objname = classname()
# samsung = feature_phone()
# samsung.calling("samsung")
# samsung.message(1234567890)


# nokia = feature_phone()
# nokia.calling("nokia")
# nokia.message(1564984964)

# celkon = feature_phone()
# celkon.calling("celkon")
# celkon.message(149849614)





# class feature_phone():
#     def __init__(self,brand,color,battery=3000):
#         self.brand = brand
#         self.color = color
#         self.battery = battery
#     def calling(self,):
#         print(f"you are calling from {self.brand}")
#     def message(self):
#         print(f"message has been sent successfully ")
# samsung = feature_phone("samsung","color",)
# samsung.calling()
# samsung.message()


# nokia = feature_phone("nokia","black","2500mah")
# nokia.calling()

# celkon = feature_phone("celkon","red","5000mah")
# celkon.calling()



# class feature_phone():
#     def __init__(self,brand,color,battery):
#         self.brand = brand
#         self.color = color
#         self.battery = battery
#     def calling(self,):
#         print(f"you are calling from {self.brand}")
#     def message(self):
#         print(f"message has been sent successfully ")

# class smart_phones(feature_phone):
#     def browsing(self,broswer):
#         print(f"browsing from {broswer}")
#     def photo_capture(self):
#         print(f"photo captureed..")
# samsung = smart_phones("samsungs26","titanum",6000)
# samsung.calling()
# samsung.message()
# samsung.browsing("chrome")
# samsung.photo_capture()





# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")
# obj = b()
# obj.parent()
# obj.child1()
# obj2 = c()
# obj2.parent()
# obj2.child2()










# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")

# obj = child()
# obj.father()
# obj.mother()
# obj.child()






class gfather():
    def output(self):
        print(f"earned 100cr properties")
class father(gfather):
    def output1(self):
        print(f"this is father class")
class child(father):
    def output2(self):
        print(f"this is child class")
    def sample(self):
        print(f"started ABC company")
obj = child()
obj.output()
obj.output1()
obj.output2()
obj.sample()





# class ATM():
#     def __init__(self,bank,branch,location,balance=1000):
#         self.bank = bank
#         self.branch = branch
#         self.location = location
#         self.balance = balance
#     def credit(self):
#         pass
# class ATM2(ATM):
#     def withdraw(self):
#         pass
#     def balance(self):
#         pass
#     def pin(self):
#         pass
# SBIN = ATM("SBIN","tadepalligudem","mainroad",)
# while True:
#     print(1.)
#     print(1.)
#     print(1.)
#     print(1.)
#     print(1.)
#     choice = input("enter the choice: ")
#     if choice == "1":
#         SBIN.credit()


