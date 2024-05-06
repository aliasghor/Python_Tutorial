"""
    A map() function will return an iterator from the specified function to each every item in an iterable.

    The differences between iterator and iterable are:
    an iterable is a data structures/collections, such as: List, Sets, Dictionary, Tuples, Strings. Whereas an iterator is an object that we get after looping through the entire iterable.
"""

# An examples and the usage of map() function

def iterableLength(iterable):
    """A function to count an iterable length"""
    return len(iterable)

data = ["Gerry","Mogi","Sampi"]
map_result = map(iterableLength,data)

for index, value in enumerate(map_result):
    print(f"{data[index]} has a name length for about = {value} characters")

data = list(range(10 + 1))
map_result = map(lambda num: num * 2,data)
print(list(map_result))