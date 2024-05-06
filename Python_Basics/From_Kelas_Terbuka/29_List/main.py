# List is a built in data structure in Python.And a list is NOT an array,although they act or share the same similarties but in the end they aren't the same

# A group list of numbers
list_numbers = [1,2,3,4,5]
print(f"List numbers: {list_numbers}")

# A group list of strings
list_strings = ["Gerry","Mogi","Pace"]
print(f"List strings: {list_strings}")

# Creating a range sequance of numbers and then cast it into a list
data_range = range(1,10,2)
print(f"Creating a range sequance of numbers and then cast it into a list: {list(data_range)}")

# Using list comprehension
list_comprehension = [i for i in range(10)]
print(f"Using list comprehenssion = {list_comprehension}")

# Using list comprehension and a condition
list_comprehension = [i for i in range(10 + 1) if i % 2 == 1]
print(f"Using list comprehenssion and a condition = {list_comprehension}")