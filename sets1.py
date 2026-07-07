# sample = {1,}
# print(sample)
# print(type(sample))

# sample_2 = set()
# print(sample_2)
# print(type(sample_2))


# sample = {"santhosh","pythonlife",390,56.78,887,("simple","sets",38)}
# print(sample)

# sample = {"pythonlife",389,5.7,87}
# sample.add((1,2,3,4))
# print(sample)

# sample = {"pythonlife",389,5.7,87}
# sample.clear()
# print(sample)

# sample = {"pythonlife",389,5.7,87}
# sample_2 = sample.copy()
# sample_2.add("hello everyone")
# print(sample_2)
# print(sample)


# sample = {"pythonlife",389,5.7,87}
# obj = sample.pop()
# print(sample)
# print(obj)

# sample = {"pythonlife",389,5.7,87}
# new = {1,2,3,4,5,6,7,"pythonlife"}
# sample.update(new)
# print(sample)









######################## may 14 2026 ##################

# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.union(set_2)
# print(set_3)




# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.intersection(set_2)
# print(set_3)



# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.symmetric_difference(set_2)
# print(set_3)



# set_1 = {1,2,3,4,5}
# set_2 = {6,7,8,9,1}
# set_3 = set_1.isdisjoint(set_2)
# print(set_3)


# set_1 = {1,2,3,4,5}
# set_2 = {1,4,5,6,7,8,9}
# set_3 = set_1.difference(set_2)
# print(set_3)


# set_1 = {1,2,3,4,5}
# set_2 = {1,2,3,4}
# print(set_1.issuperset(set_2))
# print(set_2.issubset(set_1))


# voter_data = {"santhosh","sree ram","raju","kumar",}
# voter_data_2 = {"santhosh","sree ram","raju","kumar","bhanu","bharat",}
# print(voter_data_2.issuperset(voter_data))
# print(voter_data.issubset(voter_data_2))



# set_1 = {1,2,3,4}
# set_1.add(5)
# print(set_1)

# set_1 = {1,2,3,4}
# set_2 = frozenset(set_1)
# print(set_1.union(set_2))
# set_2.add(5)
# print(set_2)



# Exercise

#  Set Intersection
# Write Python code to find and print the intersection of the following two sets
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = set1.intersection(set2)
# print(set3)


# Set Union
# Write Python code to find and print the union of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8,9,10}
# set3 = set1.union(set2)
# print(set3)

# Set Difference
# Write Python code to find and print the elements present in set1 but not in 
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = set1.difference(set2)
# print(set3)


# Set Symmetric Difference
# Write Python code to find and print the symmetric difference of the following
# two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3 = set1.symmetric_difference(set2)
# print(set3)

#  Set Membership Test

# Write Python code to check if the element 3 is present in the set my_set :
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)