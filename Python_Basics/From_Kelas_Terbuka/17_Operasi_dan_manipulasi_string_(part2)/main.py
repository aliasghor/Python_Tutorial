# Merubah semua ke uppercase
print(20 * "=" + " Merubah semua ke uppercase " + 20 * "=")
nama = 'ali'
print(f"nama normal: {nama}")
print(f"nama tidak normal: {nama.upper()}")

# Merubah semua ke lowercase
print(20 * "=" + " Merubah semua ke lowercase " + 20 * "=")
nama = 'ALI'
print(f"nama normal: {nama}")
print(f"nama tidak normal: {nama.lower()}")

# Pengecekan dengan is method
print(20 * "=" + " Pengecekan dengan is method " + 20 * "=")
nama = 'ali'
print(f"Apakah {nama} adalah lowercase? jawabannya = {nama.islower()}")
print(f"Apakah {nama} adalah uppercase? jawabannya = {nama.isupper()}")

# isalpha() <- untuk mengecek semuanya huruf
# isalnum() <- untuk mengecek huruf dan angka
# isdecimal() <- untuk mengecek angka saja
# isspace() <- untuk mengecek spasi, tab dan new line \n
# istitle() <- untuk mengecek judul.semua huruf harus diawali dengan huruf besar

judul = 'Harry Potter The Golbert And Fire'
cek_judul = judul.istitle()
print(f"Apakah {judul} memenuhi syarat istitle()? jawabannya = {cek_judul}")

# Cek komponen startswith() dan endswith()
print(20 * "=" + " Cek komponen startswith() dan endswith() " + 20 * "=")
nama = "Ali Masyhuri Asghor"
cek_start = nama.startswith("Ali")
cek_end = nama.endswith("Ali")
print(f"Hasil boolean startswith() = {cek_start}")
print(f"Hasil boolean endswith() = {cek_end}")

# Penggabungan komponen join() dan Memisahkan komponen split()
print(20 * "=" + " Penggabungan komponen join() dan Memisahkan komponen split() " + 20 * "=")

data = ['Aku','Sayang','Kamu']
print(data)

data_gabungan = ' '.join(data)
print(data_gabungan)

data_gabungan = ' Sumpah '.join(data)
print(data_gabungan)

split = data_gabungan.split(' Sumpah ')
print(split)

# ljust() center() rjust()
print(20 * "=" + " lcenter() rcenter() rjust() " + 20 * "=")

center = "tengah".center(10,'-')
print("'" + center + "'")

kiri = "kiri".ljust(10,'-')
print("'" + kiri + "'")

kanan = "kanan".rjust(10,'-')
print("'" + kanan + "'")

# strip()
print(20 * "=" + " strip() " + 20 * "=")
kanan = kanan.strip('-')
print("'" + kanan + "'")