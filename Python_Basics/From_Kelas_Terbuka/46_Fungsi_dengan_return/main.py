def factorial(num):
    """A function that performs a factorial calculation"""
    if num == 1:
        print(num,'=',end=' ')
        return 1
    
    else:
        print(num,'*',end=' ')
        return num * factorial(num - 1)
        

result_factorial = factorial(5) # Every return value that is inside of factorial function will get stored in this variable
print(result_factorial)

print(factorial(10)) # Every return value that is inside of factorial function will get called here

# Function that called many return values
def mathematics_operations(num1, num2):
    add = num1 + num2
    multiply = num1 * num2
    division = num1 / num2
    power = num1 ** num2
    substract = num1 - num2

    return add, multiply, division, power, substract

add, multiply, division, power, substract = mathematics_operations(5,10) # Each return value will get stored in each of these variables
print(f"The result of add = {add}")
print(f"The result of multiply = {multiply}")
print(f"The result of division = {division}")
print(f"The result of power = {power}")
print(f"The result of substract = {substract}")