# Operator assignments for numbers
print(20 * "=" + " Operator assignments for numbers " + 20 * "=")
x = 10
x += 1
print(f"Value x after being added (+= 1) =  {x}")

x -= 3
print(f"Value x after being substracted (-= 1) =  {x}")

x *= 2
print(f"Value x after being multiplied (*= 2) =  {x}")

x //= 2
print(f"Value x after being floor division (//= 2) =  {x}")

x /= 2
print(f"Value x after being divided (/= 2) =  {x}")

x **= 2
print(f"Value x after being exponented (**= 2) =  {x}")

x %= 2
print(f"Value x after being moded (%= 2) =  {x}")

# Operator assignment for boolean
# OR
print(20 * "=" + " Operator assignment for boolean " + 20 * "=")
boolean = True

boolean |= False
print(f"Boolean value after being or = {boolean}")

boolean = True

boolean &= False
print(f"Boolean value after being and = {boolean}")

boolean = True

boolean ^= True
print(f"Boolean value after being xor = {boolean}")

# Operator bitwise assignment
print(20 * "=" + " Operator bitwise assignment " + 20 * "=")
binary_number = 0b00000100

# Shifting operator
binary_number >>= 1
print(f"{binary_number} after being shifted to the right = {binary_number} and the binary number is: {format(binary_number,'08b')}")

binary_number <<= 2
print(f"{binary_number} after being shifted to the left = {binary_number} and the binary number is: {format(binary_number,'08b')}")

