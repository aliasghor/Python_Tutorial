# Contoh pertama untuk pengunaan execption
print(20 * "=" + " Contoh pertama untuk pengunaan execption " + 20 * "=")

def bagi(num1: int, num2: int) -> int:
    """Fungsi untuk melakukan sebuah pembagian"""
    return num1 // num2

angka1 = int(input("Masukan angka pertama: "))
angka2 = int(input("Masukan angka kedua: "))

try:
    hasil_pembagian = bagi(angka1,angka2)
    print(f"Hasil pembagian = {hasil_pembagian}")
    
except:
    print(f"Error angka2 tidak boleh {angka2}")

# Contoh kedua untuk pengunaan execption
print("\n" + 20 * "=" + " Contoh kedua untuk pengunaan execption " + 20 * "=")

try:
    with open("data.txt",mode='r') as read_file:
        print(read_file.read())

except:
    print("Error data.txt tidak ditemukan membuat data.txt baru")
    with open("data.txt",mode='w',encoding='utf-8') as write_file:
        write_file.write("Menuliskan file baru")