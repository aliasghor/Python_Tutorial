nama = "Gerry"

tebak_nama = input("Silahkan tebak nama: ")

if tebak_nama == nama:
    print(f"Betul!! tebakan anda {tebak_nama}")

elif tebak_nama == 'Manto':
    print(f"{tebak_nama} siapa?")

else:
    print(f"Maaf aku gk kenal kamu {tebak_nama}")

tebak_angka = int(input("Hasil dari 1 + 1 = "))

if tebak_angka == 2:
    print(f"Salah!!! hasil dari 1 + 1 bukan!! {tebak_angka}")

else:
    print(f"Betul hasil dari 1 + 1 = {tebak_angka}")

print("Program Selesai")

