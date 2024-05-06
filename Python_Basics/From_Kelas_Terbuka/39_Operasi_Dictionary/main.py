# Operator dictionary

data_dict  = {
    "Name":"Ali",
    "Age":20,
    "Citizen Of":"Indonesia",
    "University":"University Of Wollongong"
}

print(data_dict)

# Panjang Dictionary
panjang_dict = len(data_dict)
print(f"Panjang dictionary = {panjang_dict}")

# Cek Key Exist Apa Tidak
University = "University"
cek_key = University in data_dict
print(f"Apakah {University} ada di data dict? = {cek_key}")

# Menggunakan method dalam operasi dictionary
print("\n" + 20 * "=" + " Menggunakan method dalam operasi dictionary " + 20 * "=")
print(f"Menggunakan method get() {data_dict.get("name","Key tidak ditemukan")}")

print(f"Menggunakan method update() {data_dict.update({"Places That Has Been Visited":["Switzerland","Bali","Malaysia","Singapore"]})}")

print(data_dict)

# Tidak menggunakan method dalam operasi dictionary
print("\n" + 20 * "=" + " Tidak menggunakan method dalam operasi dictionary " + 20 * "=")

print(f"Menggunakan square brackets untuk melakukan indexing: {data_dict['Name']}")

data_dict['Name'] = 'Ali Asghor'

print(f"Menggunakan square brackets untuk mengganti key: {data_dict}")