"""
    *args or arguments will return a tuple.and you can pass many arguments as you want to
"""

# An example usage of *args

def sumFunction(*numbers: int) -> int:
    """A function that accepts many arguments as you want and then sum all of the arguments"""
    result = sum(numbers)
    return result

sum_result = sumFunction(1,2,3,4,5)
print(f"Your sum result is = {sum_result}")

def proveThatArgsWillReturnTuple(*args: any) -> tuple:
    """A function just to prove that this function will return a tuple"""
    print(args)

proveThatArgsWillReturnTuple(1,2,3,"Gerry",True)

def absent(*students):
    for index, value in enumerate(students):
        print(f"{index + 1}. {value}")

absent("Gerry","Mogi","Pace","Balu","APooh")
