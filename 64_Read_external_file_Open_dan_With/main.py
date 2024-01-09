print(20 * "=" + " Membaca file dengan text " + 20 * "=")

# Membaca file seluruh baris harus menggunakan method read()

file = open("data.txt",mode='r')

# print(file.read())

# Membaca file baris-sebaris harus menggunakan method readline()

# By default print funtion akan enter sebuah baris dan begitu juga dengan data text ketika kita membuat baris baru di data text by default sudah enter.jadi kita harus override argument atau parameter end

# print(file.readline(),end='')
# print(file.readline(),end='')

# Membaca file seluruh baris sebagai list harus menggunakan method readlines()

print(file.readlines())

# Apakah file bisa dibaca?
print(f"Apakah file bisa dibaca? = {file.readable()}")

# Apakah file bisa ditulis?
print(f"Apakah file bisa ditulis? = {file.writable()}")

# Apakah file sudah diclose?

print(f"Apakah file bisa diclose? = {file.closed}")
file.close()
print(f"Apakah file bisa diclose? = {file.closed}")

# Membaca file dengan keyword with
print("\n" + 20 * "=" + " Membaca file dengan keyword with " + 20 * "=")

# By default ketika menggunakan teknik ini file akan otomatis di closed ketika keluar dari scope indentation akan tetapi masih False kita masih berada di lingkup scope indentation
with open("data.txt",mode='r') as file:
    content = file.read()
    print(content)
    print(f"Apakah file bisa diclose? = {file.closed}")

print(f"Apakah file bisa diclose? = {file.closed}")