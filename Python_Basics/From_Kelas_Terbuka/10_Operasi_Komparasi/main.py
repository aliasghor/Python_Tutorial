"""
    Macam-Macam operasi komparasi
    1. >
    2. >=
    3. <
    4. <=
    5. ==
    6. !=
    7. is
    8. is not
"""

# Lebih besar dari (>)
print(20 * "=" + " Lebih besar dari (>) " + 20 * "=")
x = 5
y = 10

hasil = x > 3
print(f"{x} > 3 = {hasil}")

hasil = y > 5
print(f"{y} > 5 = {hasil}")

# is sebagai komparasi object identity
x = 5
y = 5

print(f"Nilai x = {x} id = {hex(id(x))}")
print(f"Nilai y = {y} id = {hex(id(y))}")

# Kurang dari (<)
print(20 * "=" + " Lebih besar dari (<) " + 20 * "=")
x = 5
y = 10

hasil = x < 3
print(f"{x} < 3 = {hasil}")

hasil = y < 5
print(f"{y} < 5 = {hasil}")

# Kurang dari sama dengan (<=)
print(20 * "=" + " Kurang dari sama dengan (<=) " + 20 * "=")
x = 5
y = 10

hasil = x <= 3
print(f"{x} <= 3 = {hasil}")

hasil = y <= 5
print(f"{y} <= 5 = {hasil}")

# Lebih dari sama dengan (>=)
print(20 * "=" + " Lebih dari sama dengan (>=) " + 20 * "=")
x = 5
y = 10

hasil = x >= 3
print(f"{x} >= 3 = {hasil}")

hasil = y >= 5
print(f"{y} >= 5 = {hasil}")

# Tidak sama dengan (!=)
print(20 * "=" + " Tidak sama dengan (!=) " + 20 * "=")
x = 5
y = 10

hasil = x != 3
print(f"{x} != 3 = {hasil}")

hasil = y != 5
print(f"{y} != 5 = {hasil}")

# sama dengan (==)
print(20 * "=" + " Tidak sama dengan (==) " + 20 * "=")
x = 5
y = 10

hasil = x == 3
print(f"{x} == 3 = {hasil}")

hasil = y == 5
print(f"{y} == 5 = {hasil}")

# is sebagai operasi komparasi object identity
print(20 * "=" + " is " + 20 * "=")
x = 5
y = 5

print(f"Nilai x = {x} id = {hex(id(x))}")
print(f"Nilai y = {y} id = {hex(id(y))}")

hasil = x is y
print(f"Is {x} is equals to {y}? the answer is: {hasil}")


# is not sebagai operasi komparasi object identity
print(20 * "=" + " is not " + 20 * "=")

x = 5
y = 5

print(f"Nilai x = {x} id = {hex(id(x))}")
print(f"Nilai y = {y} id = {hex(id(y))}")

hasil = x is not y
print(f"Is {x} is not equals to {y}? the answer is: {hasil}")