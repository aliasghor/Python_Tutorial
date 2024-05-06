# Pengunaan type hints

"""
    A type hints is just a "hint" to the interpreter wheter we pass on the arguments that does not match like the type hints it will not generate an error to the interpreter it self

    unless if we do it like this

    def powerTo(num: int) -> int:
        hasil = num ** 2
        return hasil

    hasil = powerTo("Gerry")  <- The interpreter it self do not care if we passed on the arguments that does not match the criteria.but it will be a problem if we run the code
    print(f"Your power result is = {hasil}")

"""


# The correct way using type hints

# Using a factorial function that has a type hints of int and the return value of this function "must" be an integer although the interpreter it self not forcing you to use an integer
def factorial(num: int) -> int:
    """
        Factorial function that has a an arguments of an integer and the return value is an integer too
    """
    if num == 1:
        print(num,'=',end=' ')
        return 1
    
    else:
        print(num,'*',end=' ')
        return num * factorial(num - 1)
    
factorial_result = factorial(10)
print(f"{factorial_result:,}")

# Using a "void" function
def greet(name: str) -> None:
    """A void function that is used to greet someone"""
    print(f"Hello {name}")

greet("Gerry")
greet("Mogi")

# Using type hints in OOP paradigm

class Person:

    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def display(self) -> None:
        """A method to display all of the attributes"""
        print(f"{self.name} is {self.age} years old and has a salary for about {self.salary}")

gerry = Person("Gerry",10,3500.555)
gerry.display()