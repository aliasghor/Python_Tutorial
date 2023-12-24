data_list_biasa = ["Gerry","Mogi","Sparky"]

print(f"Data list biasa = {data_list_biasa}")

# Data list 2 dimensi
print(20 * "=" + " Data list 2 dimensi " + 20 * "=")
data_2d = [[1,2,3],[4,5,6]]
print(f"Data list 2 dimensi = {data_2d}")

# Indexing data list 2 dimensi
print("\n" + 20 * "=" + " Indexing data list 2 dimensi " + 20 * "=")

# Mengambil array pertama dan element pertama
print(f"Mengambil array pertama = {data_2d[0]}")
print(f"Mengambil array pertama dan elemen pertama = {data_2d[0][0]}")

# Mengambil array terakhir dan element terakhir
print(f"Mengambil array pertama = {data_2d[-1]}")
print(f"Mengambil array pertama dan elemen pertama = {data_2d[-1][-1]}")

# Contoh penggunaan array 2d
print("\n" + 20 * "=" + " Contoh penggunaan array 2d " + 20 * "=")
peserta1 = ["Gerry",15,"Laki-Laki"]
peserta2 = ["Mogi",10,"Perempuan"]
peserta3 = ["Sampi",5,"Perempuan"]

peserta_gabungan = [peserta1,peserta2,peserta3]

for peserta in peserta_gabungan:
    print(f"Nama peserta: {peserta[0]}")
    print(f"Umur peserta: {peserta[1]}")
    print(f"Jenis-Kelamin peserta: {peserta[2]}\n")
