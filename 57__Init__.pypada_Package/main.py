from science import *
import science.array

add_result = math.add(1,2,3,4,5)
print(f"Addtion result is = {add_result}")

multiplication_result = math.multiplication(1,2,3,4,5)
print(f"Multiplication result is = {multiplication_result}")

power_to_result = math.power_to(5,5)
print(f"5 power to 5 is = {power_to_result:,}")


reversing_array = science.array.array_reverse([1,2,3,4,5])
print(f"Reversed array = {reversing_array}")