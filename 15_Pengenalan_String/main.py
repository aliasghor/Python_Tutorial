# 1. Cara membuat string

"""
    1. Bisa menggunakan single quote
    2. Bisa menggunakan single double quote
"""

data = 'Bisa menggunakan single quote'
print(data)

data = "Bisa menggunakan double quote"
print(data)

# 2. Menggunakan tanda (\,\n,\t,\b,\')

# Menggunakan tanda \'
print("Mari sholat Juma\'t")

# Menggunakan backslash \
print("C:\\Coding\\Python")

# Menggunakan tab
inputNama = input("Menggunakan tab:\t")

print(f"Nama antum: {inputNama}")

# Menggunakan backspace
print("Gerry \bMogi")

# Menggunakan newline
print("\nLF(Line Feed)")
print("\rCr(Carriage Return)")
print("\r\nCrlf(Carriage Return Line Feed)")

# Menggunakan raw string
print(r'C:\gerry')