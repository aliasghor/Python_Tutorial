# List available methods for an object string
print(50 * "=" + " List available methods for an object string " + 50 * "=")
print(dir(""))

# 1. Menyambung string concatenate
print("\n\n" + 50 * "=" + " 1. Menyambung string concatenate " + 50 * "=")
nama_awal = "Ali"
nama_tengah = "Masyhuri"
nama_akhir = "Asghor"

nama_lengkap = nama_awal + " " + nama_tengah + " " + nama_akhir
print(f"Nama lengkap: {nama_lengkap}")

# 2. Menghitung panjang string
print("\n\n" + 50 * "=" + " 2. Menghitung panjang string " + 50 * "=")
panjang = len(nama_lengkap)
print(f"Panjang nama_lengkap: {panjang} spasi dihitung!!")

# 3. Cek komponen karakter didalam string
print("\n\n" + 50 * "=" + " 3. Cek komponen karakter didalam string " + 50 * "=")
A = 'A'
status = A in nama_lengkap
print(f"Apakah {A} ada di dalam {nama_lengkap}? jawabannya = {status}")

status = A not in nama_lengkap
print(f"Apakah {A} tidak ada di dalam {nama_lengkap}? jawabannya = {status}")

# 4. Index string
print("\n\n" + 50 * "=" + " 3. Index string " + 50 * "=")

print(f"Index ke 0: {nama_lengkap[0]}")
print(f"Index ke 1: {nama_lengkap[1]}")
print(f"Index ke-1: {nama_lengkap[-1]}")
print(f"Index ke[0:4]: {nama_lengkap[0:4]}")
print(f"Index ke[0:10:2]: {nama_lengkap[0:10:2]}")

# Item paling kecil
print("\n\n" + 50 * "=" + " 5. Item terkecil dan terbesar " + 50 * "=")
print(f"Item terkecil dari {nama_lengkap} adalah: {min(nama_lengkap)}")

# Item paling kecil
print(f"Item terbesar dari {nama_lengkap} adalah: {max(nama_lengkap)}")

asciiCode = ord(" ")
print(f"Ascii code untuk spasi adalah = {asciiCode}")

asciiCode = ord("y")
print(f"Ascii code untuk y adalah = {asciiCode}")

data_ascii = 65

# 6. Operator untuk methods string
print("\n\n" + 50 * "=" + " 6. Operator untuk methods string " + 50 * "=")

data = "ali asghor"
a = 'a'
jumlah_a = data.count(a)
print(f"jumlah {a} dalam {data} = {jumlah_a}")