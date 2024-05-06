import dis

def factorial(n):
    if n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)
    
factorial_result = factorial(5)
print(f"Factorial of 5 is = {factorial_result}")
dis.dis(factorial)