# Standard library Python

# datetime
print(20 * "=" + " Menggunakan module datetime " + 20 * "=")
import datetime

waktu_sekarang = datetime.datetime.now()
print(f"Waktu sekarang: {waktu_sekarang}")
print(f"Hari sekarang: {waktu_sekarang:%A}")
# print(f"Hari sekarang: {waktu_sekarang.strftime("%A")}") <- cara lain untuk mengeluarkan waktu sekarang ini
print(f"Tahun sekarang = {waktu_sekarang.year}")
print(f"Hari sekarang = {waktu_sekarang.day}")
print(f"Bulan sekarang = {waktu_sekarang.month}")

# Menggunakan module collections
print("\n" + 20 * "=" + " Menggunakan module collections " + 20 * "=")
from collections import Counter
data_angka = (1,2,3,1,2,3,4,5,6,7,8,9,0,1,2,3,8,9,3,5,3)

print("Mencari angka 1 dengan membuat algoritmnya secara eksplisit")

count = 0

for i in data_angka:
    if i == 1:
        count += 1

print(f"Data nomor 1 berjumlah = {Counter(data_angka)}")

loop_dict = Counter(data_angka)

for key, value in loop_dict.items():
    print(f"{key} : {value}")

hitung = Counter(data_angka)

print(f"Jumlah angka yang paling banyak muncul = {hitung.most_common(3)}")

# Menggunakan module io
print("\n" + 20 * "=" + " Menggunakan module io " + 20 * "=")
import io

baca_data = io.open("bacaData.txt",'r')

print(baca_data.read())