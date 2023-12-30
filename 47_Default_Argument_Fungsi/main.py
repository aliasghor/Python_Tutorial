# Default argument

# Example 1
def greet(name="Gerry"):
    """A function that has only 1 default argument"""
    print(f"Hi {name}")

greet("Ali ganteng")
greet()

# Example 2
def add(num1,num2=5):
    """
        A function that has only 1 default argument and 1 parameter
        Tip if a function has combination of 1 default argument and 1 parameter
        you must put the default argument on the last parameter otherwise it doesn't work
    """
    hasil = num1 + num2
    return hasil # <- return the hasil keyword to the function call

add_result = add(10,5)
print(add_result)

add_result = add(10)
print(add_result)

# Example 3
def factorial(n):
    """
        A factorial function that you can change the parameter on the argument when you invoked the factorial function
    """
    if n == 1:
        print(n,'=',end=' ') # <- changing the parameter of end at the print function
        return 1
    
    else:
        print(n,'*',end=' ')
        return n * factorial(n - 1)
    
factorial_result = factorial(5)
print(factorial_result)

factorial_result = factorial(n=10)
print(factorial_result)

# Example 4
def power(num1=5,num2=5):
    """
        A power function that has 2 default parametes and feel free to change the default parameters on the arguments
    """
    result_power = num1 ** num2
    return result_power

result_power = power(num2=10) # You can do it in unordered way
print(f"The power result is = {result_power}")