# Python filter() function is used to process (filtered) an iterable and extract those items that satisfy a given condition.

# An examples usage of Python filter() function using def and lambda functions:

# Using lambda function
is_even = map(lambda iter: iter %2 == 0,[0,1,2,3,4,5,6,7,8,9,10])
print(list(is_even))

# Using def function
def is_positive(iter):
    return iter > 0

result = map(is_positive,[-1,-2,5,-4,-10,1,2,-5,9,-7,-9])
print(list(result))
