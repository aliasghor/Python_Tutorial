# List is a data structure variable that can contain any kind of data types.

# A simple examples the usage of list:

empty_list = []

# .append() method will "append" or add a value to the end of the list.
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)

print(f"List after being appended = {empty_list}")

# Looping through the entire list using for loop

for num in empty_list:
    print(num)

# Creating a list that can have any data types
data_list = [True,"Ali ganteng",3.141592653589,-5]

"""
    Looping through the entire list using enumarte() function,
    will result an index and value.
"""

for index, value in enumerate(data_list):
    print(f"Index {index} has a value of {value}")

# Looping 2 lists using zip() function
students_name = ["Gerry","Mogi","Sampi"]
gpa = [4.00,3.9,3.85]

for list1, list2 in zip(students_name,gpa):
    print("{0} has a GPA of = {1}".format(list1,list2))

