"""
    In prior python, python uses a format strings like in C programming language.
    the "%" operator is used to formatted a strings.
"""

# An examples of format strings
name = "Ali ganteng"

print("Hello, %s!" % name)

# To use two or more arguments specifiers, use tuple.
name = "Ali ganteng"
age = 20

print("Hello, %s you are %d years old" % (name,age))

# Any object which is not a string can be formatted using %s specifier as well.
my_list = list(range(5))

print("List = %s" % my_list)

# To formatted a floating decimal numbers we can use the %f specifier.
pi = 3.141592653589

print("Pi last 2 digit numbers = %.2f" % pi)
