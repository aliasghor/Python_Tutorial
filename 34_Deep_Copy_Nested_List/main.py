data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,5]
data_2D_copy = data_2D.copy()
print(data_2D)
print(data_2D_copy)

# Memory address data_2D dan data_2D_copy
print("\n" + 20 * "=" + " Memory address data_2D dan data_2D_copy " + 20 * "=")
print(f"Memori address data_2D = {hex(id(data_2D))}")
print(f"Memori address data_2D_copy = {hex(id(data_2D_copy))}")
print(f"Memori address list pertama dalam list data_2D_copy = {hex(id(data_2D_copy[0]))}")
print(f"Memori address list pertama dalam list data_2D_ = {hex(id(data_2D[0]))}")

# Mengubah element pada list pertama bersama dengan elementnya
print(20 * "=" + " Mengubah element pada list pertama bersama dengan elementnya " + 20 * "=")
data_2D_copy[0][0] = 100
data_2D_copy[2] = 1000

print(data_2D)
print(data_2D_copy)

# deepcopy
from copy import deepcopy
print("\n" + 20 * "=" + " deepcopy " + 20 * "=")

data_2D = [data_0,data_1,5]
data_2D_copy = data_2D.copy()
data_2D_deepCopy = deepcopy(data_2D)

print(f"Memori address data_2D = {hex(id(data_2D))}")
print(f"Memori address data_2D_copy = {hex(id(data_2D_copy))}")
print(f"Memori address data_2D_deepCopy = {hex(id(data_2D_deepCopy))}")

print(f"Data Asli = {hex(id(data_2D[0]))}")
print(f"Data Copy = {hex(id(data_2D_copy[0]))}")
print(f"Data DeepCopy = {hex(id(data_2D_deepCopy[0]))}")

data_2D[0][0] = 1500
data_2D[2] = 100
print(data_2D)
print(data_2D_copy)
print(data_2D_deepCopy)
