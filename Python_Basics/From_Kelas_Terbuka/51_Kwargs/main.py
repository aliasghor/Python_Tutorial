"""
    **kwargs will always return a dictionary
"""

def kwargsFunction(**kwargs):
    """A function to prove that kwargs will return a dictionary"""
    print(kwargs)

kwargsFunction(name="Ali",age=20)

def identity(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

identity(name="Ali",age=20,citizen="Indonesia",visited_place=["Switzerland","Bali","Malaysia","Singapore"])

def identity(**kwargs):
    name = kwargs['name']
    age = kwargs['age']

    print(f"{name} is {age} years old")

identity(name='Gerry',age=7)

def calculate(*args,**kwargs):
    num = 0

    if kwargs['option'] == 'add':
        print("Addition operation")

        for i in args:
            num += i

    elif kwargs['option'] == 'multiply':
        print("Multiplication operation")
        num = 1

        for i in args:
            num *= i

    else:
        print(f"Error {kwargs['option']} not found")

    return num


result_addition = calculate(1,2,3,4,5,option='add')
print(f"Addition result = {result_addition}")

result_multiplication = calculate(1,2,3,4,5,option='multiply')
print(f"Multiplication result = {result_multiplication}")