import time

start_time = time.time()

def factorial(n):
    if n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)
    
hasil = factorial(20)

print(f"Your factorial result is: {hasil}")

print(f"The duration of the execution program is: {time.time() - start_time} seconds")