"""
    Operasi logika boolean
    - not
    - or
    - and
    - xor(^)
"""

# not
print(20 * "=" + " not " + 20 * "=")
a = True
hasil = not a

print(f"{a} if we not the result will be = {hasil}")

# or
print("\n" + 20 * "=" + " or " + 20 * "=")
x = True
y = True
hasil = x or y
print(f"{x} or {y} the result will be = {hasil}")

x = True
y = False
hasil = x or y
print(f"{x} or {y} the result will be = {hasil}")

x = False
y = True
hasil = x or y
print(f"{x} or {y} the result will be = {hasil}")

x = False
y = False
hasil = x or y
print(f"{x} or {y} the result will be = {hasil}")

# and
print("\n" + 20 * "=" + " and " + 20 * "=")
x = True
y = True
hasil = x and y
print(f"{x} and {y} the result will be = {hasil}")

x = True
y = False
hasil = x and y
print(f"{x} and {y} the result will be = {hasil}")

x = False
y = True
hasil = x and y
print(f"{x} and {y} the result will be = {hasil}")

x = False
y = False
hasil = x and y
print(f"{x} and {y} the result will be = {hasil}")

# xor
print("\n" + 20 * "=" + " xor " + 20 * "=")
x = True
y = True
hasil = x ^ y
print(f"{x} ^ {y} the result will be = {hasil}")

x = True
y = False
hasil = x ^ y
print(f"{x} ^ {y} the result will be = {hasil}")

x = False
y = True
hasil = x ^ y
print(f"{x} ^ {y} the result will be = {hasil}")

x = False
y = False
hasil = x ^ y
print(f"{x} ^ {y} the result will be = {hasil}")
