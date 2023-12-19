"""
    study case homework
    1. -----0++++++5-------8+++++11------
    2. +++++0------5+++++++8------11++++++
"""

# No.1
print("Case study homework question number 1")
print(" 1. -----0++++++5-------8+++++11------\n")

inputUser = int(input("Please insert a number like the shown example above especially on number 1: "))

angka1 = inputUser >= 0 and inputUser <= 5
print(f"The result boolean of the first number is: {angka1}")

angka2 = inputUser >= 8 and inputUser <= 11
print(f"The result boolean of the second number is: {angka2}")

result = angka1 or angka2
print(f"The boolean result of the two numbers is: {result}")

# No.2
print("Case study homework question number 2")
print(" 2. +++++0------5+++++++8------11++++++\n")

inputUser = int(input("Please insert a number like the shown example above especially on number 2: "))

angka1 = inputUser <= 0 or inputUser >= 5
print(f"The result boolean of the first number is: {angka1}")

angka2 = inputUser <= 8 or inputUser >= 11
print(f"The result boolean of the second number is: {angka2}")

result = angka1 and angka2
print(f"The boolean result of the two numbers is: {result}")