"""
    __main__ is a top level code environment.a top level code environment is an "entry point" to the program

    In other programming languages like C++,C,Java etc.they do have an entry program from "main" where the code will start executing from that main function

    whereas Python we do not need to type an entry point of the program.although it is not needed it is consider good to add main program when we need to split our programs into a module or a package
"""



# Print out the value of dunder __name__
print(f"The value of __name__ from main.py and running directly is = {__name__}") # The result will be __main__ because we run the program directly without being imported.this will tell "us" as a programmer when we see an if __name__ == '__main__' that module is an entry point of the program

# Importing a module that has __name__
import exampleMainByModule

