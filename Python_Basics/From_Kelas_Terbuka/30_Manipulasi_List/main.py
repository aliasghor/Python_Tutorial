data_list = ["Gerry","Mogi","Sparky","Balu"]
print(f"Data list: {data_list}")

# Mengambil index
print(20 * "=" + " Mengambil index " + 20 * "=")
print(f"Mengambil index ke 0: {data_list[0]}")
print(f"Mengambil index ke 2: {data_list[2]}")
print(f"Mengambil index ke - 1: {data_list[-1]}")
print(f"Mengambil index ke - 3: {data_list[-3]}")

# Mencari sebuah nama didalam list(in)
print("\n" + 20 * "=" + " Mencari sebuah nama didalam list(in) " + 20 * "=")
Balu = "Balu"
status = Balu in data_list
print(f"Apakah ada {Balu} didalam {data_list}? Jawabnnya = {status}")

# Insert sebuah element baru(insert)
print("\n" + 20 * "=" + " Insert sebuah element baru(insert) " + 20 * "=")
data_list.insert(2,"Sampi")
print(f"Data setelah di insert = {data_list}")

# Append sebuah element baru(append)
print("\n" + 20 * "=" + " Append sebuah element baru(append) " + 20 * "=")
data_list.append("Manto")
print(f"Data setelah di append = {data_list}")

# Menambah data baru(extend)
data_list = ["Gerry","Mogi","Sparky","Balu"]
print("\n" + 20 * "=" + " Menambah data baru(extend) " + 20 * "=")
data_baru = ["Wellem","Romy","Muchsin"]
data_list.extend(data_baru)
print(f"Data setelah di extend = {data_list}")

# Remove sebuah data atau elements(remove)
print("\n" + 20 * "=" + " Remove sebuah data atau elements(remove) " + 20 * "=")
data_list.remove("Romy")
print(f"Data setelah di remove = {data_list}")
