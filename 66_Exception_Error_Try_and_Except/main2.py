import os
from numbers import Number

# Contoh ketiga pengunaan exception
print(20 * "=" + " Contoh ketiga pengunaan exception " + 20 * "=")

def calculate(num1,option,num2):
    match option:
        case '+':
            result = num1 + num2

        case '-':
            result = num1 - num2

        case '/':
            result = num1 / num2

        case 'x' | '*':
            result = num1 * num2

        case _:
            print(f"Error unknown {option}")

    return result

while True:
    os.system("cls")
    try:
        num1 = int(input("Please input your first number: "))
        option = input("Please choose your option (+,-,x,/): ")
        num2 = int(input("Please input your first number: "))

        result = calculate(num1,option,num2)
        print(f"Your result is = {result}")


    except Exception as e:
        print(e)
        os.system("pause")

    is_done = input("Do you want to exit from this program? (Y/N): ")

    if is_done == 'y' or is_done == 'Y':
        break
print("Program finished")

def factorial(num: int) -> int:
    if not isinstance(num,Number):
        raise "Error anda harus memasukan argumentnya sebagai integer atau float selain dari itu adalah salah!!"
    
    elif num == 1:
        print(num,'=',end=' ')
        return 1

    else:
        print(num,'x',end=' ')
        return num * factorial(num - 1)
    
hasil_factorial = factorial(15)
print(f"{hasil_factorial:,}")