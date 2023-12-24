import os

# Program List Buku
print(20 * "=" + " Program List Buku " + 20 * "=")
list_buku = []
while True:
    os.system("cls")
    judul_buku = input("Masukan judul buku: ")
    nama_penulis = input("Masukan nama penulis buku: ")

    data_buku = [judul_buku,nama_penulis]
    list_buku.append(data_buku)

    print(f"{'Nomor Buku':^15} {'Judul Buku':^20} {'Penulis Buku':^20}")
    for index, value in enumerate(list_buku):
        print(f"{index + 1:^15} {value[0]:^20}  {value[1]:^20}")

    is_quit = input("Apakah anda mao keluar dari program ini (Y/N) ")

    if is_quit == 'Y' or is_quit == 'y':
        os.system("cls")
        break

print("Program selesai")