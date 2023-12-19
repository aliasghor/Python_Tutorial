# Tipe data integer
print(50 * "=" + "Tipe data integer" + 50 * "=")

angka_int = 50
print(f"Angka integer = {angka_int} dan memiliki tipe data = {type(angka_int)}")

# Tipe data float
print("\n" +50 * "=" + "Tipe data float" + 50 * "=")
tipe_data_float = 3.141592653589
print(f"Angka float = {tipe_data_float} dan memiliki tipe data = {type(tipe_data_float)}")

# Tipe data string
print("\n" +50 * "=" + "Tipe data string" + 50 * "=")
tipe_data_string = "Ini adalah string"
print(f"Tipe data string = {tipe_data_string} dan memiliki tipe data = {type(tipe_data_string)}")

# Tipe data boolean atau biner
print("\n" +50 * "=" + "Tipe data boolean" + 50 * "=")
tipe_data_boolean = True
print(f"Tipe data string = {tipe_data_boolean} dan memiliki tipe data = {type(tipe_data_boolean)}")

# Tipe data complex
print("\n" +50 * "=" + "Tipe data complex" + 50 * "=")
tipe_data_complex = complex(5,10)
print(f"Tipe data string = {tipe_data_complex} dan memiliki tipe data = {type(tipe_data_complex)}")

# Tipe data import dari bahasa C
from ctypes import c_longlong, c_char
print("\n" +50 * "=" + "Tipe data import dari bahasa C" + 50 * "=")
tipe_data_dari_bahasa_C_cLongLong = c_longlong(500000)
print(f"Tipe data long long dari bahasa C = {tipe_data_dari_bahasa_C_cLongLong} dan memiliki tipe data = {type(tipe_data_dari_bahasa_C_cLongLong)}")

tipe_data_cChar = c_char(120)
print(f"Tipe data char dari bahasa C = {tipe_data_cChar} dan memiliki tipe data = {type(tipe_data_cChar)}")

