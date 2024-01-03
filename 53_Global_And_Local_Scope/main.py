# Global and Local scope examples

# Global scope example

# 1. Accesing global variables through function,loop and an if statement
print(20 * "=" + "  1. Accesing global variables through function,loop and an if statement " + 20 * "=")

global_variable = "Gerry"

def sayHello():
    print(f"Hello {global_variable} your name is called in a function")

sayHello()
print('\n')

i = 0

while i < 5:
    print(f"Hello {global_variable} your name is called in a while loop")
    i += 1

print('\n')

if True:
    print(f"Hello {global_variable} your name is called inside an if statement")

# 2. Second example of a global scope
print(20 * "=" + "  2. Second example of a global scope " + 20 * "=")
def greet():
    print(f"Hello {name} how are you?")

name = "Ali Ganteng"

greet()

num = 5
change_name = "Tikus"

def changeGlobalVariables(change_num,change_previous_name):
    global num
    global change_name

    num = change_num
    change_name = change_previous_name


print(f"{num} and {change_name} before being changed")
changeGlobalVariables(10,"Ali Ganteng banget YaAllah")
print(f"{num} and {change_name} after being changed")

# 3. Local scope example

"""
    def localScope():
        nama = "Ali is so handsome"

    print(nama) <- this print function cannot access local variable called nama
"""