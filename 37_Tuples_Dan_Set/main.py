# List
data_list = [1,2,3,4,5]
print(f"Data list = {data_list} memiliki tipe data = {type(data_list)}")

# Tuples
data_tuples = 1, 2, 3, 4, 5, 5
print(f"Data tuples = {data_tuples} memiliki tipe data = {type(data_tuples)}")
print(data_tuples[0])

jumlah_5_di_tuples = data_tuples.count(5)
print(f"Jumlah angka 5 di {data_tuples} = {jumlah_5_di_tuples}")

jumlah_5_di_tuples = data_tuples.count(5)
print(f"Jumlah angka 5 di {data_tuples} = {jumlah_5_di_tuples}")

# Sets
data_sets = {1, 2, 3, 3 , 4, 5}
print(f"Data sets = {data_sets} memiliki tipe data = {type(data_sets)}")

pop_data_sets = data_sets.pop()

print(f"Data sets setelah di popped {data_sets} = {pop_data_sets}")