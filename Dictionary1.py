# sample_dictionary = {}
# print(sample_dictionary)
# print(type(sample_dictionary))


# sample_dictionary_2 = dict()
# print(sample_dictionary_2)
# print(type(sample_dictionary_2))



# sample_dictionary_3 = {1:"santhosh",2:"charan",3:"suman",4:"kumar"}
# print(sample_dictionary_3)


# sample = {
#     "user1":"user1@123",
#     "user2":"user2@123",
#     1:"Vasu",
#     2:"kiran",
#     (1,3):"sai",
#     2:"pythonlife",
#     3:"sai",
#     4:[1,2,3,4],
#     5:(1,2,3),
# }
# print(sample)


# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1.clear()
# print(dictionary_1)




# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# sample = dictionary_1.copy()
# print(sample)
# sample.clear()
# print(sample)

# print(dictionary_1)




# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# print(dictionary_1.items())
# print(dictionary_1.keys())
# print(dictionary_1.values())



# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# sample_data = {
#     "user5":"user5@123",
#     "user6":"user6@123",
#     "user7": "user7@123",
#     "user8": "user8@123"
# }

# dictionary_1.update(sample_data)
# print(dictionary_1)


# print(sample_data)







# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# print(dictionary_1.get("user3"))
# print(dictionary_1["user3"])
# print(dictionary_1.get("user1"))
# print(dictionary_1["user1"])





# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# print(dictionary_1.get("user5"))
# # print(dictionary_1["user5"])






# list_1 = [10,20,30,40]
# print(list_1[2])







# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# obj = dictionary_1.pop("user2")
# print(dictionary_1)
# print(obj)



# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# dictionary_1["user5"] = "user5@123"
# dictionary_1["user2"] = "pythonlife"
# print(dictionary_1)



# user_name = input("enter the username: ")
# password = input("enter the password")
# user_data = {}
# user_data[user_name] = password
# print(user_data)

# user_data = {}
# for i in range(10):
#     user_name = input("enter the username: ")
#     password = input("enter the password")
#     user_data[user_name] = password

# print(user_data)


# dictionary_1 = {
#     "user1" : "user1@123",
#     "user2" : "user2@123",
#     "user3" : "user3@123",
#     "user4" : "user4@123",
# }
# for i,j in dictionary_1.items():
#     print(i,j)



# dictionary_1 = {}
# word = input("Enter the word: ").lower()
# meaning = input("enter the meaning: ")
# dictionary_1[word] = meaning
# print(dictionary_1)




# Exercise#
# Write Python code to add a new key-value pair to the following dictionary
# my_dict = {"name": "Santhosh", "age": 22}
# sample_data = {"city_name":"nandyal","location":"nandyal"}
# my_dict.update(sample_data)
# print(my_dict)
# print(sample_data)


# Write Python code to access and print the value associated with the key 'price' in the following dictionary
# Dictionary
# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "brand": "Dell"
# }
# print(product["price"])


# Write Python code to remove the key-value pair with the key 'city' from the following dictionary
# my_dict = {'name': 'santhosh', 'age': 22, 'city': 'nandyal'}
# del my_dict['city']
# print(my_dict)

# Write Python code to print all the keys present in the following dictionary:
# my_dict = {'name': 'santhosh', 'age': 22, 'city': 'nandyal'}
# print(list(my_dict.keys()))


# Write Python code to print all the values present in the following dictionary
# my_dict = {'name': 'santhosh', 'age': 22, 'city': 'nandyal'}
# print(list(my_dict.values()))


# Exercise 1: Dictionary Update
# Write a Python script that updates a dictionary with a new key-value pair.
# Original dictionary

# student = {
#     "name": "Santhosh",
#     "age": 22
# }
# student["city"] = "Nandyal"
# print(student)

# Exercise 2: Dictionary Access
# Write a Python script that accesses and prints the value associated with a specific 
# key in a dictionary.

# employee = {
#     "id": 101,
#     "name": "Santhosh",
#     "salary": 50000
# }
# print(employee["name"])


# Exercise 3: Dictionary Removal
# Write a Python script that removes a key-value pair from a dictionary.

# student = {
#     "name": "Santhosh",
#     "age": 22,
#     "city": "Nandyal"
# }
# del student["city"]
# print(student)

# Exercise 4: Dictionary Keys
# Write a Python script that prints all the keys present in a dictionary
# employee = {
#     "id": 101,
#     "name": "Santhosh",
#     "department": "IT"
# }
# print(employee.keys())

# Exercise 5: Dictionary Values
# Write a Python script that prints all the values present in a dictionary
employee = {
    "id": 101,
    "name": "Sree ram",
    "department": "IT"
}
print(employee.keys())