import os

def hitungLuas(panjang,lebar):
    hasil = panjang * lebar
    return hasil

def hitungKeliling(panjang,lebar):
    hasil = 2 * (panjang + lebar)
    return hasil


while True:
    os.system("cls")
    print("Selamat datang di program menghitung luas dan keliling persegi panjang")
    print("Silahkan pilih opsi anda dibawah ini",end='\n\n')

    print("1.Menghitung luas persegi panjang")
    print("2.Menghitung keliling persegi panjang")
    print("3.Keluar dari program",end='\n\n')

    pilih = int(input("Pilih opsi anda disini: "))

    if pilih == 1:
        os.system("cls")
        print("Bagus anda ingin menghitung luas persegi panjang")
        print("Silahkan masukan nilai panjang dan lebarnya dibawah ini")
        print(60 * "=")
        masukan_panjang = int(input("Silahkan masukan panjang persegi panjang: "))
        masukan_lebar = int(input("Silahkan masukan lebar persegi panjang: "))

        hasil_luas = hitungLuas(masukan_panjang,masukan_lebar)
        print(f"Hasil luas persegi panjang = {hasil_luas}")
        os.system("pause")

    elif pilih == 2:
        os.system("cls")
        print("Bagus anda ingin menghitung keliling persegi panjang")
        print("Silahkan masukan nilai panjang dan lebarnya dibawah ini")
        print(60 * "=")
        masukan_panjang = int(input("Silahkan masukan panjang persegi panjang: "))
        masukan_lebar = int(input("Silahkan masukan lebar persegi panjang: "))
        
        hasil_Keliling = hitungKeliling(masukan_panjang,masukan_lebar)
        print(f"Hasil Keliling persegi panjang = {hasil_Keliling}")
        os.system("pause")


    elif pilih == 3:
        os.system("cls")
        break

    else:
        os.system("cls")
        print(f"Error angka {pilih} tidak ada!!")
        os.system("pause")

print("Program selesai")