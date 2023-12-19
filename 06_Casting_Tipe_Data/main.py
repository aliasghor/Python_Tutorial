# Casting tipe data string menjadi tipe data yang bukan string
print("\n" + 20 * "=" + "Casting tipe data string menjadi tipe data yang bukan string" + 20 * "=")
data_string = "0"

print(f"Data string = {data_string} dan memiliki tipe data  = {type(data_string)}")

merubah_data_string_menjadi_integer = int(data_string)
print(f"Setelah merubah string menjadi data integer = {merubah_data_string_menjadi_integer} dan memiliki tipe data  = {type(merubah_data_string_menjadi_integer)}")

merubah_data_string_menjadi_float = float(data_string)
print(f"Setelah merubah string menjadi data float = {merubah_data_string_menjadi_float} dan memiliki tipe data  = {type(merubah_data_string_menjadi_float)}")

merubah_data_string_menjadi_boolean = bool(int(data_string))
print(f"Setelah merubah string menjadi data boolean = {merubah_data_string_menjadi_boolean} dan memiliki tipe data  = {type(merubah_data_string_menjadi_boolean)}")

# Casting tipe data int menjadi tipe data yang bukan int
print("\n" + 20 * "=" + "Casting tipe data int menjadi tipe data yang bukan int" + 20 * "=")
data_integer = 1

print(f"Data integer = {data_integer} dan memiliki tipe data  = {type(data_integer)}")

merubah_data_integer_menjadi_string = str(data_integer)
print(f"Setelah merubah integer menjadi data string = {merubah_data_integer_menjadi_string} dan memiliki tipe data  = {type(merubah_data_integer_menjadi_string)}")

merubah_data_integer_menjadi_float = float(data_integer)
print(f"Setelah merubah integer menjadi data float = {merubah_data_integer_menjadi_float} dan memiliki tipe data  = {type(merubah_data_integer_menjadi_float)}")

merubah_data_integer_menjadi_boolean = bool(int(data_integer))
print(f"Setelah merubah integer menjadi data boolean = {merubah_data_integer_menjadi_boolean} dan memiliki tipe data  = {type(merubah_data_integer_menjadi_boolean)}")

# Casting tipe data float menjadi tipe data yang bukan float
print("\n" + 20 * "=" + "Casting tipe data int menjadi tipe data yang bukan int" + 20 * "=")
data_float = 3.141592653589

print(f"Data float = {data_float} dan memiliki tipe data = {type(data_float)}")

merubah_data_float_menjadi_string = str(data_float)
print(f"Setelah merubah float menjadi data string = {merubah_data_float_menjadi_string} dan memiliki tipe data  = {type(merubah_data_float_menjadi_string)}")

merubah_data_float_menjadi_integer = int(data_float)
print(f"Setelah merubah integer menjadi data float = {merubah_data_float_menjadi_integer} dan memiliki tipe data  = {type(merubah_data_float_menjadi_integer)}")

merubah_data_float_menjadi_boolean = bool(float(data_float))
print(f"Setelah merubah integer menjadi data boolean = {merubah_data_float_menjadi_boolean} dan memiliki tipe data  = {type(merubah_data_float_menjadi_boolean)}")

# Casting tipe data boolean menjadi tipe data yang bukan boolean
print("\n" + 20 * "=" + " Casting tipe data boolean menjadi tipe data yang bukan boolean" + 20 * "=")
data_boolean = True

print(f"Data boolean = {data_boolean} dan memiliki tipe data = {type(data_boolean)}")

merubah_data_boolean_menjadi_string = str(data_boolean)
print(f"Setelah merubah boolean menjadi data string = {merubah_data_boolean_menjadi_string} dan memiliki tipe data  = {type(merubah_data_boolean_menjadi_string)}")

merubah_data_boolean_menjadi_integer = int(data_boolean)
print(f"Setelah merubah boolean menjadi data int = {merubah_data_boolean_menjadi_integer} dan memiliki tipe data  = {type(merubah_data_boolean_menjadi_integer)}")