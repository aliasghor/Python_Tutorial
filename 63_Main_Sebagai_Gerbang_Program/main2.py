# Importing a module
from module import add
import package

# Creating the top level code environment

def main():   # <- this function called main is just to encapsulates every program within it
    addition_result = add(5,5)
    print(f"Addition result = {addition_result}")

    data_list = [1,1,1,2,3,4,5,6,7,8,9,10,10,10,1,2,3,4,5]
    find_num_1 = package.findCommonNumbers(data_list,1)
    print(f"Number 1 is showed = {find_num_1} times")

if __name__ == '__main__':
    main() # <- we invoked the main function here and just in case when we accidentally import the main program the main program script do not get executed because we encapsulates every main source code file within the main function and within the if __name__ == '__main__' statement too