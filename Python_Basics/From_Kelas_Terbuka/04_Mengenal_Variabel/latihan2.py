# This the second file exercise regarding 04_Mengenal_Variabel.

"""
    A variable is used to hold value to the variable it self. In addition a variabel is a name memory location where the computer stores our value, to assign a value to the variable we'll need to use assignment operator (=). Below is an example how to store a value to a variable. Every variables (objects) in Python has it's own unique id (id is the object's memory address) to get the unique id of a variables (objects) we'll need to use id() function.
"""

# Create a variable called "variable" and assigns it with a value of -1000.
variable = -1000
print(f"variable has a value of = {variable:,}, varriable memory address = {id(variable)}")

# Naming variables convention

# Use camel case naming convention
camelCase = "Using camelCase"
print(camelCase)

# Use under score naming convention
under_score = "Using under_score"
print(under_score)

# Use an integer value behind the variable name
var10 = 10
print(var10)