# String
print(20 * "=" + " String " + 20 * "=")
nama = "Ali"
format_str = f"Nama: {nama}"
print(format_str)

# Numbers
print(20 * "=" + " Numbers " + 20 * "=")
pi = 3.141592653589
format_str = f"Angka pi: {pi:.2f}"
print(format_str)

angka_ribuan = 1000000000
format_str = f"Angka ribuan: {angka_ribuan:,}"
print(format_str)


# Boolean
print(20 * "=" + " Boolean " + 20 * "=")
boolean = True
format_str = f"Boolean: {boolean}"
print(format_str)

# Menampilkan leading zero
print(20 * "=" + " Menampilkan leading zero " + 20 * "=")
angka = 1005.5555
format_str = f"Angka: {angka:010.2f}"
print(format_str)

# Format persen
print(20 * "=" + " Format persen " + 20 * "=")
percentage = 0.045
format_str = f"Angka: {percentage:.2%}"
print(format_str)

# Format angka(binary, octal, hexadecimal)

angka = 255

format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hexadecimal = f"Hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)