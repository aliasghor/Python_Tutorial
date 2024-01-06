import numpy as np

data_list = [1,2,3,4,5]
data_array = np.array([1,2,3,4,5])
print(f"Data list = {data_list}")
print(f"Data array = {data_array}")

# Melakukan operasi matematika
# print(f"Data list di pangkat 2 = {data_list**2}") <- data_list tidak bisa di pangkat
print(f"Data array dipangkat 2 = {data_array**2}")
print(f"Data list di kalikan 2 = {data_list * 2}")
print(f"Data array di kalikan 2 = {data_array * 2}")

# Membuat sebuah matrix
matrix = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(matrix)

matrix_zeros = np.zeros((2,5))
print(matrix_zeros)

matrix_ones = np.ones((2,5))
print(matrix_ones)
