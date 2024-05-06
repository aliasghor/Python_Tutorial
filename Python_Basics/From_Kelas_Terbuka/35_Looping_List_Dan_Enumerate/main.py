# Menggunakan loop for
print(20 * "=" + " Menggunakan loop for " + 20 * "=")
kumpulan_angka = [1,2,3,4,5]

for angka in kumpulan_angka:
    print(f" Menggunakan loop for: {angka}")


# Menggunakan loop for range() dan len()
print(20 * "=" + " Menggunakan loop for range() dan len() " + 20 * "=")
kumpulan_angka = [1,2,3,4,5]

for angka in range(len(kumpulan_angka)):
    print(f"Index: {angka} value: {kumpulan_angka[angka]}")

# Menggunakan while loop dan len()
print(20 * "=" + " Menggunakan while loop dan len() " + 20 * "=")
kumpulan_angka = [1,2,3,4,5]

angka = 0

while angka < len(kumpulan_angka):
    print(f"Index: {angka} value: {kumpulan_angka[angka]}")
    angka += 1

# Menggunakan list comprehenssion
print(20 * "=" + " Menggunakan list comprehenssion " + 20 * "=")
kumpulan_angka = [1,2,3,4,5]

list_comprehenssion = [angka for angka in kumpulan_angka]
print(list_comprehenssion)

# Menggunakan enumerate()
print(20 * "=" + " Menggunakan enumerate() " + 20 * "=")
kumpulan_angka = ["Gerry","Mogi","Pace","Balu","Manto"]

for index, value in enumerate(kumpulan_angka):
    print(f"Index: {index} value: {value}")
